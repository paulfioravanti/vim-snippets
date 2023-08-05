# Vim Snippets

This is my collection of [Vim][] snippets, for use with [Ultisnips][].

Their original home was in [my dotfiles][] before I extracted them out into
this repository. I still use [rcm][] to symlink my `.vim` directory to the
snippets, which requires the top-level `vim` directory here.

Trigger words for snippets are typically short words or mnemonics (see
[`honza/vim-snippets`][]), but many of mine tend to be whole words or phrases,
since I use them primarily with [Plover][] stenography (see
[my stenography dictionaries][]), which enables that easily.

## Dependencies

Some of my snippets leverage [`px.snippets`][] helpers from the
[`vim-pythonx`][] repo. If you use any of them, you will need to install
`vim-pythonx`.

## Priorities

Currently, I have the snippets in a "stack" of priorities that looks like the
following (higher priority snippets always override lower):

| Priority |                       Dictionary Type                             |
|----------|-------------------------------------------------------------------|
|  0       | Language-specific snippets                                        |
| -1       | HTML snippets                                                     |
| -2       | All snippets                                                      |

Web languages leverage HTML snippets, but they sometimes have naming clashes
with HTML, so in all general cases, the language-specific snippet should win.

## Videos

You can see the snippets in action during the following videos in my [Steno
Coding][] YouTube playlist.

[`honza/vim-snippets`]: https://github.com/honza/vim-snippets
[my dotfiles]: https://github.com/paulfioravanti/dotfiles
[my stenography dictionaries]: https://github.com/paulfioravanti/steno-dictionaries
[Plover]: https://www.openstenoproject.org/plover/
[`px.snippets`]: https://github.com/reconquest/vim-pythonx/blob/master/pythonx/px/snippets.py
[rcm]: https://github.com/thoughtbot/rcm
[Steno Coding]: https://www.youtube.com/playlist?list=PLNN5NpKrqwAMRA5uRGtGzwUDgzHFDk8Z4
[Ultisnips]: https://github.com/SirVer/ultisnips
[Vim]: https://www.vim.org/
[`vim-pythonx`]: https://github.com/reconquest/vim-pythonx
