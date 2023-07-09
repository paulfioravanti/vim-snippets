# Vim Snippets

This is my collection of [Vim][] snippets, for use with [Ultisnips][].

Their original home was in [my dotfiles][] before I extracted them out into
this repository. I still use [rcm][] to symlink my `.vim` directory to the
snippets, which requires the top-level `vim` directory here.

Trigger words for snippets are typically short words or mnemonics (see
[`honza/vim-snippets`][]), but many of mine tend to be whole words or phrases,
since I use them primarily with [Plover][] stenography (see
[my stenography dictionaries][]), which enables that easily.

## Priorities

Currently, I have the snippets in a "stack" of priorities that looks like the
following (higher priority snippets always override lower):

|                              Priorities                                      |
|------------------------------------------------------------------------------|
|  0 | Language-specific snippets                                              |
| -1 | HTML snippets                                                           |
| -2 | All snippets                                                            |

Web languages leverage HTML snippets, but they sometimes have naming clashes
with HTML, so in all general cases, the language-specific snippet should win.

## Videos

You can see the snippets in action during the following videos:

- _[Steno Coding: React Tic-Tac-Toe][]_
- _[Steno Coding: Exercism's "Luhn" challenge in Python][]_
- _[Steno Coding: TDD-ing Exercism's "Bob" challenge in Ruby][]_
- _[Stenography and Ruby][]_
- _[Stenography and Elixir][]_
- _[Build a real-time Twitter clone with steno using LiveView and Phoenix 1.6][]_
- _[Rails 7: The Steno Demo][]_

[Build a real-time Twitter clone with steno using LiveView and Phoenix 1.6]: https://www.youtube.com/watch?v=T_kMd7rxYU0
[`honza/vim-snippets`]: https://github.com/honza/vim-snippets
[my dotfiles]: https://github.com/paulfioravanti/dotfiles
[my stenography dictionaries]: https://github.com/paulfioravanti/steno-dictionaries
[Plover]: https://www.openstenoproject.org/plover/
[Rails 7: The Steno Demo]: https://www.youtube.com/watch?v=q7g0ml60LGY
[rcm]: https://github.com/thoughtbot/rcm
[Steno Coding: Exercism's "Luhn" challenge in Python]: https://www.youtube.com/watch?v=YcIwT5i9_lA
[Steno Coding: React Tic-Tac-Toe]: https://www.youtube.com/watch?v=3TDgZVIxncg
[Steno Coding: TDD-ing Exercism's "Bob" challenge in Ruby]: https://www.youtube.com/watch?v=I9Oc4AirX_0
[Stenography and Elixir]: https://www.youtube.com/watch?v=ZQO-5KfnCi4
[Stenography and Ruby]: https://www.youtube.com/watch?v=3W9_k2CXrXE
[Ultisnips]: https://github.com/SirVer/ultisnips
[Vim]: https://www.vim.org/
