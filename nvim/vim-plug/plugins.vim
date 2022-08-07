call plug#begin('~/.local/share/nvim/plugged')

" Comment code
Plug 'tpope/vim-commentary'

" Files
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'scrooloose/NERDTree' " File explorer

" Autocomplete
Plug 'sheerun/vim-polyglot'
Plug 'neoclide/coc.nvim' , { 'branch' : 'release' }
Plug 'mattn/emmet-vim'

" Format document
Plug 'prettier/vim-prettier', { 'do': 'yarn install --frozen-lockfile --production' }

" Close 
Plug 'jiangmiao/auto-pairs' " Close pairs
Plug 'alvan/vim-closetag' " Html close tags

" Supports
Plug 'pangloss/vim-javascript'    " JavaScript
Plug 'iamcco/coc-tailwindcss',  {'do': 'yarn install --frozen-l  lockfile && yarn run build'}
Plug 'rust-lang/rust.vim'   " Rust
Plug 'vim-python/python-syntax'
Plug 'pappasam/coc-jedi', { 'do': 'yarn install --frozen-lockfile && yarn build', 'branch': 'main' } "Python
Plug 'posva/vim-vue'
Plug 'yaegassy/coc-volar', {'do': 'yarn install --frozen-lockfile'}
Plug 'ekalinin/Dockerfile.vim' "Docker


" Bar
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" Icons
Plug 'ryanoasis/vim-devicons'

" Themes
Plug 'wuelnerdotexe/vim-enfocado'
Plug 'joshdick/onedark.vim'
Plug 'kaicataldo/material.vim', { 'branch': 'main' }

call plug#end()


" Python syntax
let g:python_highlight_all = 1
