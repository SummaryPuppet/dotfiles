" Turn on syntax highlight.
syntax on

set number
set relativenumber
set sw=2
set expandtab
set smartindent
set noswapfile
set clipboard=unnamedplus
set encoding=utf-8
set termguicolors
set ttyfast

syntax enable
filetype plugin indent on


" Pluggins
source ~/.config/nvim/vim-plug/plugins.vim

" Pluggins config
source ~/.config/nvim/vim-plug/plugins-config.vim

" Theme
source ~/.config/nvim/vim-plug/theme.vim


" Shortcuts 
map <C-/> <C-v>"x
:imap ii <Esc>

noremap <leader>w :w<cr>
