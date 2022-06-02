call plug#begin('~/.local/share/nvim/plugged')

" Files
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'scrooloose/NERDTree' " File explorer

" Autocomplete
Plug 'sheerun/vim-polyglot'
Plug 'neoclide/coc.nvim' , { 'branch' : 'release' }
Plug 'mattn/emmet-vim'

" Close 
Plug 'jiangmiao/auto-pairs' " Close pairs
Plug 'alvan/vim-closetag' " Html close tags

" Supports
Plug 'pangloss/vim-javascript'    " JavaScript
Plug 'leafgarland/typescript-vimleafgarland/typescript-vim' " Typescript
Plug 'iamcco/coc-tailwindcss',  {'do': 'yarn install --frozen-l  lockfile && yarn run build'}
Plug 'vim-python/python-syntax'
Plug 'rust-lang/rust.vim'   " Rust

" Theme
Plug 'dracula/vim', { 'as': 'dracula' }

call plug#end()

" Configs

" Editor 
:imap ii <Esc>

" fzf
let mapleader = ","
noremap <leader>fs :Files<cr>

" coc
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gi <Plug>(coc-implementation)

let g:coc_global_extensions = ['coc-tsserver']
" Python syntax
let g:python_highlight_all = 1

" Theme
set background=dark
let ayucolor='dark'
colorscheme dracula
