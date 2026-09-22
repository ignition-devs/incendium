"""Tests for incendium.zpl.label."""

import unittest

from tests.helpers import patch_zpl_dependencies

patch_zpl_dependencies()

from incendium.zpl.label import Label


class TestLabelInit(unittest.TestCase):
    """Tests for Label.__init__."""

    def test_default_dimensions(self):
        label = Label()
        self.assertEqual(label.height, 155)
        self.assertEqual(label.width, 105)
        self.assertEqual(label.dpmm, 8)

    def test_custom_dimensions(self):
        label = Label(height=200, width=100, dpmm=12)
        self.assertEqual(label.height, 200)
        self.assertEqual(label.width, 100)
        self.assertEqual(label.dpmm, 12)

    def test_initial_command_list(self):
        label = Label()
        self.assertEqual(label._commands, ["^XA"])


class TestLabelCode(unittest.TestCase):
    """Tests for the Label.code property."""

    def test_getter_returns_initial_zpl(self):
        label = Label()
        self.assertEqual(label.code, "^XA\n")

    def test_getter_includes_added_commands(self):
        label = Label()
        label.comment("test")
        self.assertEqual(label.code, "^XA\n^FX test\n")

    def test_getter_terminates_with_newline(self):
        label = Label()
        self.assertTrue(label.code.endswith("\n"))

    def test_setter_parses_commands(self):
        label = Label()
        label.code = "^XA\n^FX test\n^FS\n"
        self.assertEqual(label._commands, ["^XA", "^FX test", "^FS", ""])

    def test_setter_overwrites_existing_commands(self):
        label = Label()
        label.comment("old")
        label.code = "^XA\n^FX new\n"
        self.assertEqual(label._commands, ["^XA", "^FX new", ""])


class TestLabelDumpZpl(unittest.TestCase):
    """Tests for Label.dump_zpl."""

    def test_returns_complete_zpl(self):
        label = Label()
        self.assertEqual(label.dump_zpl(), "^XA\n^XZ")

    def test_includes_added_commands(self):
        label = Label()
        label.comment("test")
        self.assertEqual(label.dump_zpl(), "^XA\n^FX test\n^XZ")

    def test_ends_with_xz(self):
        label = Label()
        self.assertTrue(label.dump_zpl().endswith("^XZ"))

    def test_code_vs_dump_zpl(self):
        label = Label()
        label.comment("test")
        code = label.code
        dumped = label.dump_zpl()
        self.assertEqual(dumped, code.rstrip("\n") + "\n^XZ")


class TestLabelComment(unittest.TestCase):
    """Tests for Label.comment."""

    def test_adds_fx_command(self):
        label = Label()
        label.comment("hello")
        self.assertIn("^FX hello", label.code)

    def test_comment_with_spaces(self):
        label = Label()
        label.comment("this is a comment")
        self.assertIn("^FX this is a comment", label.code)


class TestLabelEndOrigin(unittest.TestCase):
    """Tests for Label.end_origin."""

    def test_adds_fs_command(self):
        label = Label()
        label.end_origin()
        self.assertIn("^FS", label.code)


class TestLabelFieldOrigin(unittest.TestCase):
    """Tests for Label.field_origin."""

    def test_converts_mm_to_dots(self):
        label = Label()
        label.field_origin(10, 20)
        self.assertIn("^FO80,160", label.code)

    def test_with_justification(self):
        label = Label()
        label.field_origin(10, 20, "C")
        self.assertIn("^FO80,160,C", label.code)

    def test_without_justification(self):
        label = Label()
        label.field_origin(10, 20)
        self.assertIn("^FO80,160", label.code)
        self.assertNotIn(",C", label.code.split("\n")[-2])

    def test_zero_origin(self):
        label = Label()
        label.field_origin(0, 0)
        self.assertIn("^FO0,0", label.code)


class TestLabelFieldBlock(unittest.TestCase):
    """Tests for Label.field_block."""

    def test_default_justification_and_lines(self):
        label = Label()
        label.field_block(50)
        self.assertIn("^FB400,1,0,C,0", label.code)

    def test_custom_justification_and_lines(self):
        label = Label()
        label.field_block(50, "L", 3)
        self.assertIn("^FB400,3,0,L,0", label.code)


class TestLabelFieldOrientation(unittest.TestCase):
    """Tests for Label.field_orientation."""

    def test_without_justification(self):
        label = Label()
        label.field_orientation("R")
        self.assertIn("^FWR", label.code)

    def test_with_justification(self):
        label = Label()
        label.field_orientation("R", "C")
        self.assertIn("^FWR,C", label.code)


class TestLabelChangeInternationalFont(unittest.TestCase):
    """Tests for Label.change_international_font."""

    def test_default_character_set(self):
        label = Label()
        label.change_international_font()
        self.assertIn("^CI28", label.code)

    def test_custom_character_set(self):
        label = Label()
        label.change_international_font(1)
        self.assertIn("^CI1", label.code)

    def test_with_remaps(self):
        label = Label()
        label.change_international_font(1, [(65, 66)])
        self.assertIn("^CI1,65,66", label.code)

    def test_with_multiple_remaps(self):
        label = Label()
        label.change_international_font(1, [(65, 66), (67, 68)])
        self.assertIn("^CI1,65,66,67,68", label.code)


class TestLabelGraphicBox(unittest.TestCase):
    """Tests for Label.graphic_box."""

    def test_defaults(self):
        label = Label()
        label.graphic_box(100, 50)
        self.assertIn("^GB100,50,1,B,0", label.code)

    def test_custom_parameters(self):
        label = Label()
        label.graphic_box(100, 50, 3, "W", 5)
        self.assertIn("^GB100,50,3,W,5", label.code)

    def test_line(self):
        label = Label()
        label.graphic_box(200, 1, 2)
        self.assertIn("^GB200,1,2,B,0", label.code)


class TestLabelGraphicCircle(unittest.TestCase):
    """Tests for Label.graphic_circle."""

    def test_defaults(self):
        label = Label()
        label.graphic_circle(100)
        self.assertIn("^GC100,1,B", label.code)

    def test_custom_parameters(self):
        label = Label()
        label.graphic_circle(100, 3, "W")
        self.assertIn("^GC100,3,W", label.code)


class TestLabelGraphicEllipse(unittest.TestCase):
    """Tests for Label.graphic_ellipse."""

    def test_defaults(self):
        label = Label()
        label.graphic_ellipse(100, 50)
        self.assertIn("^GE100,50,1,B", label.code)

    def test_custom_parameters(self):
        label = Label()
        label.graphic_ellipse(100, 50, 3, "W")
        self.assertIn("^GE100,50,3,W", label.code)


class TestLabelHome(unittest.TestCase):
    """Tests for Label.home."""

    def test_converts_mm_to_dots(self):
        label = Label()
        label.home(10, 20)
        self.assertIn("^LH80,160", label.code)

    def test_with_justification(self):
        label = Label()
        label.home(10, 20, "C")
        self.assertIn("^LH80,160,C", label.code)

    def test_without_justification(self):
        label = Label()
        label.home(10, 20)
        line = [l for l in label.code.split("\n") if l.startswith("^LH")][0]
        self.assertEqual(line, "^LH80,160")


class TestLabelLoadDefinition(unittest.TestCase):
    """Tests for Label.load_definition."""

    def test_adds_xf_command(self):
        label = Label()
        label.load_definition("E:TEMPLATE.FMT")
        self.assertIn("^XFE:TEMPLATE.FMT^FS", label.code)


class TestLabelModifyDarkness(unittest.TestCase):
    """Tests for Label.modify_darkness."""

    def test_positive_value(self):
        label = Label()
        label.modify_darkness(5)
        self.assertIn("^MD5", label.code)

    def test_negative_value(self):
        label = Label()
        label.modify_darkness(-10)
        self.assertIn("^MD-10", label.code)


class TestLabelPrintGraphic(unittest.TestCase):
    """Tests for Label.print_graphic."""

    def test_defaults(self):
        label = Label()
        label.print_graphic("E:LOGO.GRF")
        self.assertIn("^XGE:LOGO.GRF,1,1", label.code)

    def test_custom_magnification(self):
        label = Label()
        label.print_graphic("E:LOGO.GRF", 2, 3)
        self.assertIn("^XGE:LOGO.GRF,2,3", label.code)


class TestLabelReversePrint(unittest.TestCase):
    """Tests for Label.reverse_print."""

    def test_default_active(self):
        label = Label()
        label.reverse_print()
        self.assertIn("^LRY", label.code)

    def test_disable(self):
        label = Label()
        label.reverse_print("N")
        self.assertIn("^LRN", label.code)


class TestLabelSaveFormat(unittest.TestCase):
    """Tests for Label.save_format."""

    def test_inserts_after_start_command(self):
        label = Label()
        label.save_format("E:TEMPLATE.FMT")
        self.assertEqual(label._commands[0], "^XA")
        self.assertEqual(label._commands[1], "^DFE:TEMPLATE.FMT^FS")

    def test_preserves_subsequent_commands(self):
        label = Label()
        label.comment("before save")
        label.save_format("E:TEMPLATE.FMT")
        self.assertIn("^FX before save", label.code)
        self.assertIn("^DFE:TEMPLATE.FMT^FS", label.code)


class TestLabelSetDarkness(unittest.TestCase):
    """Tests for Label.set_darkness."""

    def test_sets_darkness(self):
        label = Label()
        label.set_darkness(20)
        self.assertIn("~SD20", label.code)


class TestLabelSetDefaultFont(unittest.TestCase):
    """Tests for Label.set_default_font."""

    def test_height_only(self):
        label = Label()
        label.set_default_font(5)
        self.assertIn("^CF0,40", label.code)

    def test_height_and_width(self):
        label = Label()
        label.set_default_font(5, 3)
        self.assertIn("^CF0,40,24", label.code)

    def test_custom_font(self):
        label = Label()
        label.set_default_font(5, 3, "A")
        self.assertIn("^CFA,40,24", label.code)


class TestLabelTextBlock(unittest.TestCase):
    """Tests for Label.text_block."""

    def test_defaults(self):
        label = Label()
        label.text_block(100, 50)
        self.assertIn("^TBN,100,50", label.code)

    def test_custom_orientation(self):
        label = Label()
        label.text_block(100, 50, "R")
        self.assertIn("^TBR,100,50", label.code)


class TestLabelBarcodeFieldDefault(unittest.TestCase):
    """Tests for Label.barcode_field_default."""

    def test_converts_mm_to_dots(self):
        label = Label()
        label.barcode_field_default(0.25, 3.0, 15)
        self.assertIn("^BY2.0,3.0,120", label.code)


class TestLabelWriteBarcode(unittest.TestCase):
    """Tests for Label.write_barcode with all barcode types."""

    def test_code39(self):
        label = Label()
        label.write_barcode(50, "3")
        self.assertIn("^B3N,N,50,Y,N", label.code)

    def test_code39_with_options(self):
        label = Label()
        label.write_barcode(50, "3", "R", "Y", "N", "Y")
        self.assertIn("^B3R,Y,50,N,Y", label.code)

    def test_qrcode(self):
        label = Label()
        label.write_barcode(50, "Q")
        self.assertIn("^BQN,2,1,Q,7", label.code)

    def test_qrcode_with_options(self):
        label = Label()
        label.write_barcode(
            50,
            "Q",
            "R",
            magnification=3,
            error_correction="H",
            mask="5",
        )
        self.assertIn("^BQR,2,3,H,5", label.code)

    def test_code128(self):
        label = Label()
        label.write_barcode(50, "C")
        self.assertIn("^BCN,50,Y,N,N,N", label.code)

    def test_code128_with_options(self):
        label = Label()
        label.write_barcode(
            50,
            "C",
            "R",
            "Y",
            "N",
            "Y",
            mode="U",
        )
        self.assertIn("^BCR,50,N,Y,Y,U", label.code)

    def test_ean(self):
        label = Label()
        label.write_barcode(50, "E")
        self.assertIn("^BEN,50,Y,N", label.code)

    def test_ean_with_options(self):
        label = Label()
        label.write_barcode(
            50,
            "E",
            "R",
            print_interpretation_line="N",
        )
        self.assertIn("^BER,50,N,N", label.code)

    def test_interleaved_2of5(self):
        label = Label()
        label.write_barcode(50, "2")
        self.assertIn("^B2N,50,Y,N,N", label.code)

    def test_code93(self):
        label = Label()
        label.write_barcode(50, "A")
        self.assertIn("^BAN,50,Y,N,N", label.code)

    def test_upca(self):
        label = Label()
        label.write_barcode(50, "U")
        self.assertIn("^BUN,50,Y,N,N", label.code)

    def test_unknown_type_adds_empty_command(self):
        label = Label()
        label.write_barcode(50, "X")
        self.assertIn("^XA\n\n^XZ", label.dump_zpl())


class TestLabelWriteFieldNumber(unittest.TestCase):
    """Tests for Label.write_field_number."""

    def test_field_number_only(self):
        label = Label()
        label.write_field_number(1)
        self.assertIn("^FN1", label.code)

    def test_with_font_parameters(self):
        label = Label()
        label.write_field_number(1, 5, 5, "0", "N")
        self.assertIn("^A0N,40,40", label.code)
        self.assertIn("^FN1", label.code)

    def test_with_line_width(self):
        label = Label()
        label.write_field_number(1, line_width=50)
        self.assertIn("^FB400,1,0,L,0", label.code)
        self.assertIn("^FN1", label.code)

    def test_with_font_and_line_width(self):
        label = Label()
        label.write_field_number(1, 5, 5, "0", "N", line_width=50)
        self.assertIn("^A0N,40,40", label.code)
        self.assertNotIn("^FB400,1,0,L,0", label.code)
        self.assertIn("^FN1", label.code)

    def test_custom_justification(self):
        label = Label()
        label.write_field_number(
            1,
            line_width=50,
            justification="C",
            max_line=3,
        )
        self.assertIn("^FB400,3,0,C,0", label.code)


class TestLabelWriteText(unittest.TestCase):
    """Tests for Label.write_text."""

    def test_text_only(self):
        label = Label()
        label.write_text("Hello")
        self.assertIn("^FDHello", label.code)

    def test_with_builtin_font(self):
        label = Label()
        label.write_text("Hello", 5, 5, "0", "N")
        self.assertIn("^A0N,40,40", label.code)
        self.assertIn("^FDHello", label.code)

    def test_with_named_font(self):
        label = Label()
        label.write_text("Hello", 5, 5, "R:MYFONT.FNT", "N")
        self.assertIn("^A@N,40,40,R:MYFONT.FNT", label.code)
        self.assertIn("^FDHello", label.code)

    def test_with_ttf_font(self):
        label = Label()
        label.write_text("Hello", 5, 5, "E:FONT_NAME.TTF", "N")
        self.assertIn("^A@N,40,40,E:FONT_NAME.TTF", label.code)
        self.assertIn("^FDHello", label.code)

    def test_with_tte_font(self):
        label = Label()
        label.write_text("Hello", 5, 5, "B:FONT.TTE", "N")
        self.assertIn("^A@N,40,40,B:FONT.TTE", label.code)
        self.assertIn("^FDHello", label.code)

    def test_with_line_width(self):
        label = Label()
        label.write_text("Hello", line_width=50)
        self.assertIn("^FB400,1,0,L,0", label.code)
        self.assertIn("^FDHello", label.code)

    def test_with_font_and_line_width(self):
        label = Label()
        label.write_text("Hello", 5, 5, "0", "N", line_width=50)
        self.assertIn("^A0N,40,40", label.code)
        self.assertIn("^FB400,1,0,L,0", label.code)
        self.assertIn("^FDHello", label.code)

    def test_custom_justification(self):
        label = Label()
        label.write_text(
            "Hello",
            line_width=50,
            justification="R",
            max_line=2,
        )
        self.assertIn("^FB400,2,0,R,0", label.code)

    def test_invalid_font_raises_error(self):
        label = Label()
        with self.assertRaises(ValueError):
            label.write_text("Hello", 5, 5, "INVALID", "N")

    def test_lowercase_letter_font_raises_error(self):
        label = Label()
        with self.assertRaises(ValueError):
            label.write_text("Hello", 5, 5, "a", "N")

    def test_multi_char_builtin_font_raises_error(self):
        label = Label()
        with self.assertRaises(ValueError):
            label.write_text("Hello", 5, 5, "00", "N")


class TestLabelIntegration(unittest.TestCase):
    """Integration tests combining multiple Label methods."""

    def test_complete_label(self):
        label = Label()
        label.set_default_font(height=5, font="0")
        label.field_origin(x=10, y=10)
        label.write_text("Title", char_height=7, char_width=7, font="0")
        label.end_origin()
        label.field_origin(x=10, y=30)
        label.graphic_box(width=83 * label.dpmm, height=1, thickness=2)
        label.end_origin()
        result = label.dump_zpl()
        self.assertTrue(result.startswith("^XA"))
        self.assertTrue(result.endswith("^XZ"))
        self.assertIn("^CF0,40", result)
        self.assertIn("^FO80,80", result)
        self.assertIn("^A0N,56,56", result)
        self.assertIn("^FDTitle", result)
        self.assertIn("^FS", result)
        self.assertIn("^GB664,1,2,B,0", result)

    def test_label_with_home_offset(self):
        label = Label()
        label.home(5, 5)
        label.field_origin(10, 10)
        result = label.dump_zpl()
        self.assertIn("^LH40,40", result)
        self.assertIn("^FO80,80", result)

    def test_multiple_commands_order(self):
        label = Label()
        label.comment("first")
        label.set_darkness(20)
        label.field_origin(10, 10)
        label.write_text("text")
        label.end_origin()
        lines = [l for l in label.code.split("\n") if l]
        self.assertEqual(lines[0], "^XA")
        self.assertEqual(lines[1], "^FX first")
        self.assertEqual(lines[2], "~SD20")
        self.assertEqual(lines[3], "^FO80,80")
        self.assertIn("^FDtext", lines[4])
        self.assertEqual(lines[5], "^FS")

    def test_zero_dimensions(self):
        label = Label()
        label.field_origin(0, 0)
        self.assertIn("^FO0,0", label.code)

    def test_large_label(self):
        label = Label(height=300, width=200, dpmm=12)
        self.assertEqual(label.dpmm, 12)
        label.field_origin(10, 10)
        self.assertIn("^FO120,120", label.code)


if __name__ == "__main__":
    unittest.main()
