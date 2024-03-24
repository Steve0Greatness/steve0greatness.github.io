title: TF2 disguise Command
date: 2022 Dec 17
updated: 2024 Jan 17

A Spy class-specific command

## Layout

The basic layout of the disguise command is very simple.

```
disguise [class] [team]
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

The reason the classes are in this order is that they were added in that order. As mentioned in [*Quake World Team Fortress* § Versions](https://wiki.teamfortress.com/wiki/Team_Fortress#Versions) on the Team Fortress wiki, it mentions the classes were added in the order of *scout*, *sniper*, *soldier*, *demoman*, and *medic*; then *heavy*; *pyro*; and finally *spy* and *engineer*.

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
