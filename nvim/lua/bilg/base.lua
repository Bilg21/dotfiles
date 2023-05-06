------------------------------
-- Bilg's NeoVim Configuration
------------------------------

-- aliases
local g = vim.g
local o = vim.o
local opt = vim.opt

o.termguicolors = true 
opt.guicursor = ""

-- Decrease update time
o.timeoutlen = 500
o.updatetime = 200

-- Number of screen lines to keep above and below the cursor when scrolling
o.scrolloff = 20

-- Better editor UI
o.number = true
o.numberwidth = 2
o.relativenumber = true
o.signcolumn = "yes"
o.cursorline = true

-- Better editing experience
o.expandtab = true
o.smarttab = true
o.cindent = true
o.autoindent = true
o.wrap = true
o.textwidth = 300
o.tabstop = 4
o.shiftwidth = 4
o.softtabstop = -1 -- If negative, shiftwidth value is used
o.list = true
o.listchars = "trail:·,nbsp:◇,tab:→ ,extends:▸,precedes:◂"

opt.hlsearch = false
opt.incsearch = true

-- Makes neovim and host OS clipboard play nicely with each other
o.clipboard = "unnamedplus"

-- Remember 50 items in commandline history
o.history = 50

-- Better buffer splitting
o.splitright = true
o.splitbelow = true

opt.mouse = "n"

-- css
-- filetype plugin on
-- set omnifunc=syntaxcomplete#Complete
