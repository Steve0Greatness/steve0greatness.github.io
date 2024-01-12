---
title: TF2 disguise Command
date: 2022 Dec 17
updated: 2022 Dec 24
---
A Spy class-specific command

## Layout

The basic layout of the disguise command is very simple.

```
disguise [class : number] [team : number]
```

## `class` Parameter

`1` : Scout

`2` : Sniper

`3` : Soldier

`4` : Demoman

`5` : Medic

`6` : Heavy

`7` : Pyro

`8` : Spy

`9` : Engineer

The reason the classes are in this order is that they were added in that order. As mentioned in the [Team Fortress wiki's article on _Quake World Team Fortress_](https://wiki.teamfortress.com/wiki/Team_Fortress#Versions)(A.K.A. _Quake Team Fortress_, or just _Team Fortress_), it mentions the classes were added in the order of _scout_, _sniper_, _soldier_, _demoman_, and _medic_; then _heavy_; _pyro_; and finally _spy_ and _engineer_.

## `team` Parameter

These depend upon what team you're on.

`-1` : Enemy Team

`-2` : Friendly Team

### Specific Teams

These aren't extremely useful, but they exist. They are independent of the team you're on. 

`1` : Blu Team

`2` : Red Team

## Example

Normally, when you disguise as a spy of your team, you undisguise. This also applies to the disguise command, allowing for an "undisguise" command.

```
disguise "8" "-2"
```

You're also able to put this into a bind, allowing for an undisguise bind.