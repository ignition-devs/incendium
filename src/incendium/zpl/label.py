"""Label builder for ZPL II printer command language.

This module provides a small, self-contained helper for assembling ZPL
II command strings. It implements ZPL II commands directly from the
publicly documented Zebra Programming Language specification.

ZPL II is a public printer command language; the command mnemonics and
syntax are documented by Zebra Technologies and are not proprietary to
any particular implementation.
"""

# A ZPL label builder exposes one method per supported command.
# pylint: disable=too-many-public-methods

__all__ = ["Label"]

import re
from typing import List, Optional, Tuple

from incendium.helper.types import AnyStr


class Label(object):
    """Build a ZPL II label format.

    Dimensions are given in millimeters unless otherwise noted and are
    converted to printer dots using the configured dots-per-millimeter
    (dpmm) resolution. The assembled command string grows as methods are
    called and can be retrieved with :meth:`dump_zpl`.
    """

    dpmm = None  # type: int
    height = None  # type: int
    width = None  # type: int

    def __init__(self, height=155, width=105, dpmm=8):
        # type: (int, int, int) -> None
        """Start a new label format.

        Args:
            height: Label height in millimeters. Defaults to 155mm
                (6.1in).
            width: Label width in millimeters. Defaults to 105mm
                (4.1in).
            dpmm: Print resolution in dots per millimeter. 8dpmm equals
                203dpi and 12dpmm equals 300dpi. Defaults to 8dpmm
                (203dpi).
        """
        self.height = height
        self.width = width
        self.dpmm = dpmm
        self._commands = ["^XA"]  # type: List[AnyStr]

    @property
    def code(self):
        # type: () -> AnyStr
        """ZPL II commands assembled so far (without the format end)."""
        return "\n".join(self._commands) + "\n"

    @code.setter
    def code(self, value):
        # type: (AnyStr) -> None
        self._commands = list(value.split("\n"))

    def _add(self, command):
        # type: (AnyStr) -> None
        """Append a command."""
        self._commands.append(command)

    def dump_zpl(self):
        # type: () -> AnyStr
        """Dump the complete ZPL II format including the end marker."""
        return "\n".join(self._commands) + "\n^XZ"

    def barcode_field_default(self, module_width, bar_width_ratio, height):
        # type: (float, float, int) -> None
        """Set the default barcode module values.

        Args:
            module_width: Narrow bar/module width in millimeters.
            bar_width_ratio: Wide-to-narrow ratio.
            height: Barcode height in millimeters.
        """
        self._add(
            "^BY{},{},{}".format(
                module_width * self.dpmm,
                bar_width_ratio,
                height * self.dpmm,
            )
        )

    def comment(self, comment):
        # type: (AnyStr) -> None
        """Insert a non-printing comment."""
        self._add("^FX {}".format(comment))

    def end_origin(self):
        # type: () -> None
        """Close the current field definition."""
        self._add("^FS")

    def field_block(self, width, justification="C", lines=1):
        # type: (int, AnyStr, int) -> None
        """Print text into a fixed-size block.

        Args:
            width: Block width in millimeters.
            justification: L, C, R or J.
            lines: Maximum number of text lines in the block.
        """
        self._add(
            "^FB{},{},0,{},0".format(
                width * self.dpmm,
                lines,
                justification,
            )
        )

    def field_origin(self, x, y, justification=None):
        # type: (int, int, Optional[AnyStr]) -> None
        """Anchor current and following fields at an origin.

        Args:
            x: Horizontal position in millimeters.
            y: Vertical position in millimeters.
            justification: Optional justification override.
        """
        command = "^FO{},{}".format(x * self.dpmm, y * self.dpmm)
        if justification is not None:
            command += ",{}".format(justification)
        self._add(command)

    def field_orientation(self, orientation, justification=None):
        # type: (AnyStr, Optional[AnyStr]) -> None
        """Set the default field orientation.

        Args:
            orientation: N, R, I or B.
            justification: Optional default justification override.
        """
        command = "^FW{}".format(orientation)
        if justification:
            command += ",{}".format(justification)
        self._add(command)

    def change_international_font(
        self,
        character_set=28,  # type: int
        remaps=None,  # type: Optional[List[Tuple[int, int]]]
    ):
        # type: (...) -> None
        """Change the international font/encoding.

        A remap entry is a (source_character, destination_character)
        pair.

        Args:
            character_set: Desired character set number. Defaults to 28.
            remaps: Optional list of character remap pairs.
        """
        command = "^CI{}".format(character_set)
        if remaps:
            command += "," + ",".join(
                "{},{}".format(source, destination) for source, destination in remaps
            )
        self._add(command)

    def graphic_box(self, width, height, thickness=1, color="B", rounding=0):
        # type: (int, int, int, AnyStr, int) -> None
        """Draw a box or line.

        Dimensions are in dots.

        Args:
            width: Box width in dots.
            height: Box height in dots.
            thickness: Border thickness in dots.
            color: Line color, B (black) or W (white).
            rounding: Corner rounding in dots.
        """
        self._add("^GB{},{},{},{},{}".format(width, height, thickness, color, rounding))

    def graphic_circle(self, diameter, thickness=1, color="B"):
        # type: (int, int, AnyStr) -> None
        """Draw a circle.

        Dimensions are in dots.

        Args:
            diameter: Circle diameter in dots.
            thickness: Border thickness in dots.
            color: Line color, B (black) or W (white).
        """
        self._add("^GC{},{},{}".format(diameter, thickness, color))

    def graphic_ellipse(self, width, height, thickness=1, color="B"):
        # type: (int, int, int, AnyStr) -> None
        """Draw an ellipse.

        Dimensions are in dots.

        Args:
            width: Ellipse width in dots.
            height: Ellipse height in dots.
            thickness: Border thickness in dots.
            color: Line color, B (black) or W (white).
        """
        self._add("^GE{},{},{},{}".format(width, height, thickness, color))

    def home(self, x, y, justification=None):
        # type: (int, int, Optional[AnyStr]) -> None
        """Set the label home position.

        Args:
            x: Horizontal offset in millimeters.
            y: Vertical offset in millimeters.
            justification: Optional justification override.
        """
        command = "^LH{},{}".format(x * self.dpmm, y * self.dpmm)
        if justification:
            command += ",{}".format(justification)
        self._add(command)

    def load_definition(self, path):
        # type: (AnyStr) -> None
        """Load and merge a stored label format.

        Args:
            path: Storage device and image name of the label format.
        """
        self._add("^XF{}^FS".format(path))

    def modify_darkness(self, value):
        # type: (int) -> None
        """Adjust print darkness relative to the base level.

        Args:
            value: Signed adjustment between -30 and 30.
        """
        self._add("^MD{}".format(value))

    def print_graphic(self, path, magnification_x=1, magnification_y=1):
        # type: (AnyStr, int, int) -> None
        """Place a previously downloaded graphic.

        Args:
            path: Storage device and image name.
            magnification_x: Horizontal magnification, 1 to 10.
            magnification_y: Vertical magnification, 1 to 10.
        """
        self._add("^XG{},{},{}".format(path, magnification_x, magnification_y))

    def reverse_print(self, active="Y"):
        # type: (AnyStr) -> None
        """Reverse printing for the remaining format.

        Args:
            active: Y to reverse, N to disable.
        """
        self._add("^LR{}".format(active))

    def save_format(self, path):
        # type: (AnyStr) -> None
        """Save the current format to storage.

        Args:
            path: Storage device and image name to save to.
        """
        self._commands.insert(1, "^DF{}^FS".format(path))

    def set_darkness(self, value):
        # type: (int) -> None
        """Set the base print darkness level (~SD).

        Args:
            value: Base level between 0 and 30.
        """
        self._add("~SD{}".format(value))

    def set_default_font(self, height, width=None, font="0"):
        # type: (int, Optional[int], AnyStr) -> None
        """Set the default font.

        Args:
            height: Font height in millimeters.
            width: Font width in millimeters, or None for the default
                proportional width.
            font: Font name, a capital letter (A-Z) or digit (0-9).
        """
        if width is None:
            self._add("^CF{},{}".format(font, height * self.dpmm))
        else:
            self._add("^CF{},{},{}".format(font, height * self.dpmm, width * self.dpmm))

    def text_block(self, width, height, orientation="N"):
        # type: (int, int, AnyStr) -> None
        """Print justified text with a fixed block size.

        Args:
            width: Block width in dots.
            height: Block height in dots.
            orientation: N, R, I or B.
        """
        self._add("^TB{},{},{}".format(orientation, width, height))

    def write_barcode(
        self,
        height,  # type: int
        barcode_type,  # type: AnyStr
        orientation="N",  # type: AnyStr
        check_digit="N",  # type: AnyStr
        print_interpretation_line="Y",  # type: AnyStr
        print_interpretation_line_above="N",  # type: AnyStr
        magnification=1,  # type: int
        error_correction="Q",  # type: AnyStr
        mask="7",  # type: AnyStr
        mode="N",  # type: AnyStr
    ):
        # type: (...) -> None
        """Emit the field command for the requested barcode type.

        Args:
            height: Barcode height in dots.
            barcode_type: One of the supported symbologies (finally the
                ZPL ^B<symbology> command letter).
            orientation: N, R, I or B.
            check_digit: Y or N to render the check digits in text.
            print_interpretation_line: Y or N to print human-readable
                text.
            print_interpretation_line_above: Y or N to place the text
                above the barcode.
            magnification: Magnification factor, 1 to 10 (2D symbols).
            error_correction: H, Q, M or L error correction level.
            mask: Mask pattern 0 to 7.
            mode: N, U, A or D encoding mode.
        """
        command = ""

        if barcode_type == "3":
            command = "^B{}{},{},{},{},{}".format(
                barcode_type,
                orientation,
                check_digit,
                height,
                print_interpretation_line,
                print_interpretation_line_above,
            )
        elif barcode_type == "Q":
            command = "^B{}{},2,{},{},{}".format(
                barcode_type,
                orientation,
                magnification,
                error_correction,
                mask,
            )
        elif barcode_type == "C":
            command = "^B{}{},{},{},{},{},{}".format(
                barcode_type,
                orientation,
                height,
                print_interpretation_line,
                print_interpretation_line_above,
                check_digit,
                mode,
            )
        elif barcode_type == "E":
            command = "^B{}{},{},{},{}".format(
                barcode_type,
                orientation,
                height,
                print_interpretation_line,
                print_interpretation_line_above,
            )
        elif barcode_type in "2AU":
            command = "^B{}{},{},{},{},{}".format(
                barcode_type,
                orientation,
                height,
                print_interpretation_line,
                print_interpretation_line_above,
                check_digit,
            )

        self._add(command)

    def write_field_number(
        self,
        number,  # type: int
        char_height=None,  # type: Optional[int]
        char_width=None,  # type: Optional[int]
        font="0",  # type: AnyStr
        orientation="N",  # type: AnyStr
        line_width=None,  # type: Optional[int]
        max_line=1,  # type: int
        line_spaces=0,  # type: int
        justification="L",  # type: AnyStr
        hanging_indent=0,  # type: int
    ):
        # type: (...) -> None
        """Set the field for a variable from a stored format.

        Args:
            number: Field number, 0 to 9999.
            char_height: Font height in millimeters. Optional.
            char_width: Font width in millimeters. Optional.
            font: Font name (A-Z or 0-9).
            orientation: N, R, I or B.
            line_width: Maximum text line width in millimeters.
            max_line: Maximum number of text lines.
            line_spaces: Extra spacing between lines in dots.
            justification: L, R, C or J.
            hanging_indent: Hanging indent in dots.
        """
        if char_height and char_width and font and orientation:
            self._add(
                "^A{}{},{},{}".format(
                    font,
                    orientation,
                    char_height * self.dpmm,
                    char_width * self.dpmm,
                )
            )
        elif line_width:
            self._add(
                "^FB{},{},{},{},{}".format(
                    line_width * self.dpmm,
                    max_line,
                    line_spaces,
                    justification,
                    hanging_indent,
                )
            )
        self._add("^FN{}".format(number))

    def write_text(
        self,
        text,  # type: AnyStr
        char_height=None,  # type: Optional[int]
        char_width=None,  # type: Optional[int]
        font="0",  # type: AnyStr
        orientation="N",  # type: AnyStr
        line_width=None,  # type: Optional[int]
        max_line=1,  # type: int
        line_spaces=0,  # type: int
        justification="L",  # type: AnyStr
        hanging_indent=0,  # type: int
    ):
        # type: (...) -> None
        """Write a line of text as the pending field data.

        Args:
            text: The text to print.
            char_height: Font height in millimeters. Optional.
            char_width: Font width in millimeters. Optional.
            font: Font name, either A-Z/0-9 or a named font reference.
            orientation: N, R, I or B.
            line_width: Maximum text line width in millimeters.
            max_line: Maximum number of text lines.
            line_spaces: Extra spacing between lines in dots.
            justification: L, R, C or J.
            hanging_indent: Hanging indent in dots.

        Raises:
            ValueError: If a named font is invalid.
        """
        if char_height and char_width and font and orientation:
            if re.match(r"^[A-Z0-9]$", font):
                self._add(
                    "^A{}{},{},{}".format(
                        font,
                        orientation,
                        char_height * self.dpmm,
                        char_width * self.dpmm,
                    )
                )
            elif re.match(r"^[REBA]?:[A-Z0-9_]+\.(FNT|TTF|TTE)$", font):
                self._add(
                    "^A@{},{},{},{}".format(
                        orientation,
                        char_height * self.dpmm,
                        char_width * self.dpmm,
                        font,
                    )
                )
            else:
                raise ValueError("Invalid font.")
        if line_width:
            self._add(
                "^FB{},{},{},{},{}".format(
                    line_width * self.dpmm,
                    max_line,
                    line_spaces,
                    justification,
                    hanging_indent,
                )
            )
        self._add("^FD{}".format(text))
