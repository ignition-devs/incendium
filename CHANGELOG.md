# Changelog

All notable changes to this project will be documented in this file.

## [2022.2.0] - 2022-02-10

### Features

- add `get_timestamp` function ([3172d0e](https://github.com/thecesrom/incendium/commit/3172d0e72eb5eab08dd39c90a34caf0a89612b3e))

### Build

- pre-commit autoupdate (#30) ([2c877e4](https://github.com/thecesrom/incendium/commit/2c877e45c23659911dd36525c066ed22adc9f96e))

## [2.0.2] - 2022-01-25

### Refactor

- fix SonarLint and Sourcery issues ([b308e5b](https://github.com/thecesrom/incendium/commit/b308e5b2785c6dc0c907781590d1840853b3c79f))
  - **BREAKING**: stop checking instance of `in_params` and `out_params`

## [2.0.1] - 2021-12-18

### Bug Fixes

- check instance of `out_params` ([9317a9e](https://github.com/thecesrom/incendium/commit/9317a9ec051fb6ae28a4e767332c830555215bfd))

### Documentation

- fix indentation ([fee1f1e](https://github.com/thecesrom/incendium/commit/fee1f1ec12af19bc1c639a348c99cfa4b3028dd3))
- fix REPL example ([fc43f0b](https://github.com/thecesrom/incendium/commit/fc43f0b501d6699a29c003ff50ba993fe759f3a3))

### Miscellaneous Tasks

- :see_no_evil: update .gitignore file ([69bcfe4](https://github.com/thecesrom/incendium/commit/69bcfe480e6d499bb1a17be98a5872f9d57b5da6))
- add `cliff.toml` for changelog generation ([b415972](https://github.com/thecesrom/incendium/commit/b4159725f365b0286d907f4bbc7118d0af02ac48))
- format setup.cfg file ([29b91e8](https://github.com/thecesrom/incendium/commit/29b91e88c938b466fc270c6edd9cc101d438aa99))

### Styling

- set Python 2.7 as standard library ([87ebc98](https://github.com/thecesrom/incendium/commit/87ebc9865cad98c4e5fcb14f9eb742f5c8b029a8))

### Build

- update black hook ([d41f158](https://github.com/thecesrom/incendium/commit/d41f1585c5731a097a6cb9686c0442980767e818))
- pre-commit autoupdate (#28) ([e210097](https://github.com/thecesrom/incendium/commit/e210097f2fa67b43f5a0b4b624b2250e2d622d32))
- deprecate Python 2.7 ([091be5f](https://github.com/thecesrom/incendium/commit/091be5ff6339ce3ff0b7afb6ee1b7c891039449c))
- pre-commit autoupdate ([ea08729](https://github.com/thecesrom/incendium/commit/ea08729d8a96930ddf29de303537f6397d6406d6))
- pre-commit autoupdate ([55f602e](https://github.com/thecesrom/incendium/commit/55f602efa7524e11fbad0319d8100f3936a29e19))
- use Python 3.10 ([2569a5d](https://github.com/thecesrom/incendium/commit/2569a5d757076e300230ae97cc43c6140790e104))
- pre-commit autoupdate ([e1bf0a5](https://github.com/thecesrom/incendium/commit/e1bf0a5c018911bd268a277a846a1c4d8263b9b2))
- update `.pylintrc` ([0365963](https://github.com/thecesrom/incendium/commit/0365963dc5480aae6cddb08c7f92843a7756376f))
- add `setup.py` ([a28cbc4](https://github.com/thecesrom/incendium/commit/a28cbc49164fb2f88c1744ee03a9818fe993fb91))
- pre-commit autoupdate (#29) ([4396f86](https://github.com/thecesrom/incendium/commit/4396f86f7c12daa5c40da0044543c13fb02d70b5))
- add `CHANGELOG.md` to `long_description` ([59742e5](https://github.com/thecesrom/incendium/commit/59742e56be3baf42fd2aa07a02929a8b6b5dd56b))

## [2.0.0] - 2021-10-21

### Documentation

- fix typo in `Param`'s docstring ([463e96a](https://github.com/thecesrom/incendium/commit/463e96a67c5aa41237b7d34c08abc62e25903a0c))

### Features

- add InParam, OutParam and Param to db ([d6530a3](https://github.com/thecesrom/incendium/commit/d6530a3b843789373afdb48697ad44205abe958b))
  - **BREAKING**: calls to `db` functions should switch from  passing
`dict` to `list[InParam]` and `list[OutParam]` where applicable

### Miscellaneous Tasks

- update gitignore ([86868e8](https://github.com/thecesrom/incendium/commit/86868e82db1d1633eb24bf206a5b48647b254a67))
- release 2.0.0 ([1f72c46](https://github.com/thecesrom/incendium/commit/1f72c468a321a61a884681ba0db7152ebeeef9ec))

### Build

- add project_urls ([d887fac](https://github.com/thecesrom/incendium/commit/d887facc7d6ef3be76b8ffba9ac18df7622e495a))

## [1.1.2] - 2021-10-18

### Bug Fixes

- update icendium.vision.gui constants ([13af4f3](https://github.com/thecesrom/incendium/commit/13af4f39efb28ccf084b5f91796f36a02945c6e1))

### Miscellaneous Tasks

- release 1.1.2 ([94b9a30](https://github.com/thecesrom/incendium/commit/94b9a30869379f5e2b889a67cb1fa7a42f6cadec))

## [1.1.1] - 2021-10-18

### Bug Fixes

- bring back gui.CURSOR* constants ([0ebba1e](https://github.com/thecesrom/incendium/commit/0ebba1e42738de93c164fbeb374d6a48af818ab7))

### Miscellaneous Tasks

- release 1.1.1 ([1fb56ba](https://github.com/thecesrom/incendium/commit/1fb56ba1ad4f2b8a71d78ec2601ae3c571307ed0))

## [1.1.0] - 2021-10-15

### Bug Fixes

- modify Python 2 Only classifier ([1956cd7](https://github.com/thecesrom/incendium/commit/1956cd71beb10a52e62c784718430ee66ca749e6))

### CI

- add PyPI upload workflow ([d776e35](https://github.com/thecesrom/incendium/commit/d776e35f86edbcf1bc1b97a74b5dbf1fa0f056cd))

### Miscellaneous Tasks

- delete dependabot.yml ([05615d2](https://github.com/thecesrom/incendium/commit/05615d2e666ea63efafe90bd6e82cb785e8011fc))
- prepare for 1.1.0 release ([2e7a9c3](https://github.com/thecesrom/incendium/commit/2e7a9c3524f865db98e3065e267f0d75a7db5633))

### Refactor

- remove copyright from modules ([e32f032](https://github.com/thecesrom/incendium/commit/e32f032b9e3fe3e12fdcbd0b78386541bda84726))
- import unicode_literals ([63b141c](https://github.com/thecesrom/incendium/commit/63b141c68bfb202b25e5b9da6331569f0307b4be))
- import and use implementing classes rather than interfaces ([263aa71](https://github.com/thecesrom/incendium/commit/263aa712b2698fd8766ff0f7c212f3a9d9056872))
- rename `_User` class to `IncendiumUser` ([106d848](https://github.com/thecesrom/incendium/commit/106d848c3f1c15db43860f99792e807ee2e541b4))
- move version information into its own module ([bf3f464](https://github.com/thecesrom/incendium/commit/bf3f4644518778805cee5acd0488a696524c9167))

### Build

- disable `consider-using-f-string` ([722ea27](https://github.com/thecesrom/incendium/commit/722ea27633a76df72baa477679eeb0b5e5d38964))
- update black and pydocstyle hooks ([a007ffc](https://github.com/thecesrom/incendium/commit/a007ffcafd6b2e9731e3c5174de758a17b001019))
- pre-commit autoupdate ([fb4d7af](https://github.com/thecesrom/incendium/commit/fb4d7af8733fae32460ee17323d840f24a16f549))

## [1.0.7.post2] - 2021-09-13

### Documentation

- update installation instructions ([e90c07f](https://github.com/thecesrom/incendium/commit/e90c07f67d903efc44d5ae4cbdf707106c7b76d8))

## [1.0.7.post1] - 2021-09-13

### Bug Fixes

- include `__cycle__` in package `version` ([8c23ce9](https://github.com/thecesrom/incendium/commit/8c23ce9c23b146374e16b7da349c1e3e992044ac))

### Documentation

- update installation instructions ([d567ca6](https://github.com/thecesrom/incendium/commit/d567ca60a1b26ad5d9b97571a4cd0cb49f666eec))

### Miscellaneous Tasks

- update setup args ([0e63e72](https://github.com/thecesrom/incendium/commit/0e63e723f2632f7042d26887e0b0e0b4d442575d))

### Build

- remove toml dependency as it is not required ([36b638f](https://github.com/thecesrom/incendium/commit/36b638fc95d620574427a731bf82e5c0dc753eed))

## [1.0.7] - 2021-09-11

### Bug Fixes

- fix path to __version__.py ([7da881d](https://github.com/thecesrom/incendium/commit/7da881d3f2bb9524ad59a46ed1f681efe8263e8e))

### Documentation

- add instructions for installing Jython 2.7.2 ([ad4ec7a](https://github.com/thecesrom/incendium/commit/ad4ec7ac5963e91d141b3dbf8aee57969a3fc397))

### Features

- v1.0.7 ([b76db29](https://github.com/thecesrom/incendium/commit/b76db29cc6dc7e365546e5accbb37ef87c13ffb3))

### Refactor

- add pylint ([5549f0c](https://github.com/thecesrom/incendium/commit/5549f0c30ba53df6b145b57904631344524b05f9))

### Build

- bump Ignition from `6a57209` to `3a3fea8` (#20) ([b375669](https://github.com/thecesrom/incendium/commit/b375669385c37593d39824fed16a4d392f491786))
- bump Ignition from `3a3fea8` to `7262f72` (#21) ([d59a3db](https://github.com/thecesrom/incendium/commit/d59a3db2c4cef5c538de63a0911453f0958b275e))
- pre-commit autoupdate (#22) ([0214a00](https://github.com/thecesrom/incendium/commit/0214a00607ae0c1ff9f9b554ffc418d6d149e94a))
- bump Ignition from `7262f72` to `c5f1e32` (#23) ([234ebec](https://github.com/thecesrom/incendium/commit/234ebec1a916fbcb6d43e21e0bb3d8726fab5058))
- bump Ignition from `c5f1e32` to `d13416f` (#24) ([f6104fa](https://github.com/thecesrom/incendium/commit/f6104fa4474d2608735b206113dd09f4373c9b6d))
- update pylint workflow ([c30e07d](https://github.com/thecesrom/incendium/commit/c30e07d6a6f3f740a914fdea8b62d49d223ad88d))
- update pylint workflow ([75aad2d](https://github.com/thecesrom/incendium/commit/75aad2d36e9db85f60e7f45d6ee9bbb8fd8dad22))
- bump Ignition from `d13416f` to `0e80df2` (#25) ([8e14026](https://github.com/thecesrom/incendium/commit/8e14026aea53b73f812bda44184b54d18de12d17))
- bump Ignition from `0e80df2` to `3d50ca4` (#26) ([2410b3d](https://github.com/thecesrom/incendium/commit/2410b3daba41c142ed56c169ac241ee6c0fb8d43))
- remove Ignition submodule ([083ce15](https://github.com/thecesrom/incendium/commit/083ce152cc7bd838ad1e76809895d538b3b75248))
  - **BREAKING**: switching from using Ignition [jython](https://github.com/thecesrom/Ignition/tree/jython)
to installing it via `jython -m pip install`
- update CI tools ([a4e671c](https://github.com/thecesrom/incendium/commit/a4e671cd3a6bdfa7bf19314ca14ecc7e94b35e43))
- update CI workflow ([0620230](https://github.com/thecesrom/incendium/commit/06202301127570440dfb69653f995af7721875cf))

## [1.0.6] - 2021-08-05

### Bug Fixes

- break loop after expected conditions have been met ([9f0c0e7](https://github.com/thecesrom/incendium/commit/9f0c0e7ea01d76167b640a493ff57098159fbed8))

### Documentation

- update README ([23e8238](https://github.com/thecesrom/incendium/commit/23e823873a8a9086936fd555fc2123d76e4516c7))
- update README ([628d94a](https://github.com/thecesrom/incendium/commit/628d94a1c1eb42199d5cbd821f582c3b3a3856e1))
- update README.md ([7cacaef](https://github.com/thecesrom/incendium/commit/7cacaef50be417d2a059d421c16e01f585652b15))

### Refactor

- conform to snake_case naming style ([b1a41de](https://github.com/thecesrom/incendium/commit/b1a41de1e1855303f88f3ac646a88af92fcb6335))
  - **BREAKING**: `DisposableConnection`'s `db` field has been renamed to
`database` to conform with snake_case naming style and to match the name
used in some `system.db` functions.

### Build

- bump Ignition from `b63c0ad` to `172ffaa` (#11) ([843cb70](https://github.com/thecesrom/incendium/commit/843cb70168f5afbf7b3d192582f35cf132b09a31))
- pre-commit autoupdate (#13) ([8be2b75](https://github.com/thecesrom/incendium/commit/8be2b752660fefc15f246a7aab7ad86f5acc8c45))
- bump Ignition from `172ffaa` to `1a0a0b3` (#14) ([df15721](https://github.com/thecesrom/incendium/commit/df157215f00d9a83f7d44cf2224117d4de6d19b3))
- pre-commit autoupdate (#15) ([8630280](https://github.com/thecesrom/incendium/commit/8630280672da44b98232ce2828a27f1a195d117f))
- bump Ignition from `1a0a0b3` to `5247eef` (#16) ([54effa2](https://github.com/thecesrom/incendium/commit/54effa23aa0b0007580cb416b12edf4ef085bd2e))
- pre-commit autoupdate (#17) ([56dd25b](https://github.com/thecesrom/incendium/commit/56dd25bbf1b40c3ced4f9318df47a4c0464f113e))
- bump Ignition from `5247eef` to `6a57209` (#18) ([04bb5a6](https://github.com/thecesrom/incendium/commit/04bb5a60e38c6976cc11febab0a66b681eae6294))

## [1.0.5] - 2021-06-23

### Documentation

- update the copyright notice date ([65f4533](https://github.com/thecesrom/incendium/commit/65f4533d14d41da288930c8a4a171475321a88ca))
- update link to Azul Zulu ([958c9c3](https://github.com/thecesrom/incendium/commit/958c9c30cbe5ecbd59723184cd6dcc110dafcac9))
- update README ([ad29eba](https://github.com/thecesrom/incendium/commit/ad29eba3e4983cffdc924af3e42dc5016c530599))

### Features

- bump flake8 to 3.9.1 ([d7629b0](https://github.com/thecesrom/incendium/commit/d7629b0d1356d6e52a35b1b7e95efec6c3adc375))
- update black 20.8b1 -> 21.4b0 ([2fd65a7](https://github.com/thecesrom/incendium/commit/2fd65a7eed7f3c92bbf5082bad58ec2a02599e21))
- update black 21.4b0 -> 21.4b1 ([059e389](https://github.com/thecesrom/incendium/commit/059e389bd0c4cf32b944bf6a09b27c649fbe022c))
- update black 21.4b1 -> 21.4b2 ([faa2d03](https://github.com/thecesrom/incendium/commit/faa2d03060d9afc43333cf698e5fc3079a3b0e3f))
- update black 21.4b2 -> 21.5b0 ([5320e5c](https://github.com/thecesrom/incendium/commit/5320e5c406978a2c1fbcda9203d10e378e7b5d02))
- update flake8 3.9.1 -> 3.9.2 ([a17eb42](https://github.com/thecesrom/incendium/commit/a17eb420a8711ca196500bf8443c9fc2a22f2029))
- update black 21.5b0 -> 21.5b1 ([80f477a](https://github.com/thecesrom/incendium/commit/80f477a7c1db34f964378607898d434b403e3d6b))

### Miscellaneous Tasks

- update dependabot schedule interval ([35b03d9](https://github.com/thecesrom/incendium/commit/35b03d91d6615e5c5dca90c2fec548b049ea190c))
- update dependabot schedule interval ([09dd8e9](https://github.com/thecesrom/incendium/commit/09dd8e90554213fe7d4b80122bb156b1e192a430))

### Refactor

- modify imports ([3391f91](https://github.com/thecesrom/incendium/commit/3391f91e0ed0729229e0fa7ed4930e87db655c23))

### Styling

- update docstrings ([c69299c](https://github.com/thecesrom/incendium/commit/c69299c16d5adfd229dce8e8d74ab9c2614f1639))
- change from single quotes to double quotes ([06e4d2b](https://github.com/thecesrom/incendium/commit/06e4d2b160933af0ef8d4f7d639a2049a66b56c8))

### Build

- bump flake8 and isort to latest version ([5dc44b8](https://github.com/thecesrom/incendium/commit/5dc44b8051c10eb058dd4ed592957ed26d395f78))
- rearrange hooks ([4014726](https://github.com/thecesrom/incendium/commit/401472653370f538e782af3dc1e84c5f3e81d277))
- add pydocstyle hook ([a54f4b3](https://github.com/thecesrom/incendium/commit/a54f4b30ada20b3440a6bfeeaed72af9ee787a12))
- remove D209 from ignored codes ([4e5c4a1](https://github.com/thecesrom/incendium/commit/4e5c4a19b693fc96b18e073c52a38e7a9f4130b8))
- delete ignore codes ([6337f97](https://github.com/thecesrom/incendium/commit/6337f9734b7d77c891662766e49547b7e2b12edb))
- add ci block ([322f2d9](https://github.com/thecesrom/incendium/commit/322f2d9fe51332f64a5b7fba2f45a22319531684))
- pre-commit autoupdate ([b3c9e98](https://github.com/thecesrom/incendium/commit/b3c9e981b7e505395cc083098ce3c71399e3be39))
- move ci block ([9456830](https://github.com/thecesrom/incendium/commit/9456830611619337b68d9a4b0bb3901742337a6d))
- create dependabot.yml ([40c87c7](https://github.com/thecesrom/incendium/commit/40c87c7d8e07ed3bd06d47e18bc7860467f27936))
- pre-commit autoupdate (#8) ([4899d0a](https://github.com/thecesrom/incendium/commit/4899d0aed2f5aa2b6113cb49f4175ea7e8254ef8))
- bump Ignition from `b94667e` to `b1f896f` (#9) ([c7368bb](https://github.com/thecesrom/incendium/commit/c7368bb684a9e9d21b4a45a4a46a848805d08d44))
- check max complexity ([1d0617c](https://github.com/thecesrom/incendium/commit/1d0617cf1ccb84aa158168ce317fa634b775a614))
- bump Ignition from `b1f896f` to `b63c0ad` (#10) ([c284d7b](https://github.com/thecesrom/incendium/commit/c284d7b80b768b47ecc6705a23a4d9b71371f2af))

## [1.0.4] - 2021-02-25

### Features

- add flake8 pre-commit hook ([769a240](https://github.com/thecesrom/incendium/commit/769a240a0fc374f3fafba5664e2dbf91f1bf9f82))
- :sparkles: add function to convert Dataset into JSON ([ffc2157](https://github.com/thecesrom/incendium/commit/ffc21576a82820d0390c07eb81bb92f2c694fd85))

### Refactor

- :zap: simplify sequence comparison ([93b9b90](https://github.com/thecesrom/incendium/commit/93b9b90c387753af1a2255a475a36631afce7d1b))

### Styling

- Black; started tracking time with WakaTime. ([006a45c](https://github.com/thecesrom/incendium/commit/006a45c64602b0667ba07bb56d94c8b217e828ef))
- add link to Ignition Exchange ([a3cc644](https://github.com/thecesrom/incendium/commit/a3cc644caf632ef9efb6062b4d2476d23424e8a3))
- update name ([99a0bfa](https://github.com/thecesrom/incendium/commit/99a0bfaf7948428653fe76cb9c66887b99308eb0))
- :art: use isort and tell it to use Python27 ([09e7a2f](https://github.com/thecesrom/incendium/commit/09e7a2fb9ca7a8cfd8c1c874871b52fc1400dc8b))
- :art: apply some pylint fixes ([2fbf392](https://github.com/thecesrom/incendium/commit/2fbf392a1ac94c228dfd1113494f940af6f51982))

<!-- generated by git-cliff -->
