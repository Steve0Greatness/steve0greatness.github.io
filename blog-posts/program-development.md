title: Defining Development and Release Strategies of FLOSS
date: 2024 Jul 30
updated: 2025 Mar 31

Many programs are Free/Libre and Open Source, both of those
are very well defined so I'm not going to waste my or your
time by defining them for you here.

If you do need a definition, take a look at the following:

* [The Open Source Definition](https://opensource.org/osd) as
  defined by the Open Source Initiative or OSI
* [What is Free Software?](https://www.gnu.org/philosophy/free-sw.en.html)
  By the Free Software Foundation (FSF)

So without further ado, let's define developement and
release strategies!

## Development

The following is definitions for strategies used in FLOSS
development. These strategies are grouped by ones that
can't be mixed and matched.

### Who developes it?

* **Community-Driven**. Community members are able to submit patches, and these
  patches are often included directly into the project.
* **Community-Supported**. Community members are able to submit patches, but
  these patches are not included directly.
* **Non-Community-Driven**. Community members cannot submit patches.

### Does your project have (a) core maintainer(s)?

* **Unicentered**. One core maintainer.
* **Centered**. Multiple (more than one) core maintainers.
* **Non-centered**. No core maintainers.

### Do you have a full history available?

* **Historical**. A full log is available for all commits made to the project in
  question.
* **Non-Historical**. A log is not available for commits in a project.
* **Semi-Historical**. A log is available, but there is a cutoff in available
  commits.

*Note that a commit history being available doesn't mean a source history is
available, for that, see the next section.*

### When is the source code released?

* **Sourced-per-commit**. Source is made available per-commit.
* **Timed-source**. Source is released at set intervals of time.
* **Commit-based-source**. Source is released at set intervals of commits.
* **Arbitrarily-sourced**. Source is released when the maintainer(s) feel there
  has been enough changes or time, when these numbers of commits or time do not
  stay the same.

## Outro

Thank you for reading this pointless blog post. I know nobody is ever gonna get
use out of it.

## Edit: example

Google recently announced it'd be developing Andriod more privately. From the
way I've heard it described, it would seem to be historical,
arbitrarily-source, centered, and non-community-driven.

Also, SQLite would probably be historical, sourced-per-commit,
community-supported, and centered.
