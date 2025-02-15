title: Scratch is now AGPL-v3-only
date: 2024 Nov 27

[Scratch has recently relicensed](https://github.com/scratchfoundation/scratch-gui/commit/3de24da0f9e4) to the [AGPL-v3-only](https://www.gnu.org/licenses/agpl-3.0.en.html) from their previous license: the [BSD-3-Clause](https://opensource.org/license/bsd-3-clause). For all intents and purposes, this means very little. Allow me to quell some fears you may have.

## "This will kill TurboWarp!"

No. It won't. [TurboWarp is already licensed under the GPL-v3](https://github.com/TurboWarp/scratch-gui/blob/1c7850d47e0c2d50bd7ed607df8f3da40bb3bfd3/LICENSE), and by extension, so are all forks of it (ex. [LibreKitten](https://librekitten.org/)). All this means for TurboWarp is that they need to provide an easy way to get the source code of it, which it already does. So no, TurboWarp isn't going to die, it will, most likely, remain exactly the same.

## "What about projects created with Scratch?"

No version of the GPL requires documents created with software that was licensed under the GPL to also use the GPL license. As an example, images created with [GIMP](https://www.gimp.org/) do not need to be released as GPL; the same would apply to Scratch projects.

## "What about TurboWarp Packager?"

According to the [GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html#CanIUseGPLToolsForNF), you are not required to publish projects packaged with TurboWarp Packager under the AGPL.

## "Can I still sell my project/Scratch mod?"

Yes. Even assuming the AGPL applied to your project in the first place, *you can sell software licensed under any GPL license*, including the AGPL. This is because while the AGPL is a "free" license, it's not a license that mandates that anything be free of cost; in otherwords, it's free as in freedom, not free as in free of charge.

As for Scratch mods, the same applies. The AGPL isn't a non-commercial license: it's a free license.

## "What does this mean for closed source Scratch mods?"

Scratch mods that aren't open source will be required to be relicensed under the AGPL **if and only if** they pull code from Scratch in the future. This means that any Scratch mod from before Scratch's move to the AGPL will be completely fine. 

