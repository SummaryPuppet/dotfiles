call plug#begin('~/.local/share/nvim/plugged')

"Plug 'dracula/vim', { 'as': 'dracula' }
"Plug 'joshdick/onedark.vim'
"Plug 'arcticicestudio/nord-vim'
Plug 'wuelnerdotexe/vim-enfocado'

call plug#end()

set background=dark

" Dracula
"let ayucolor='dark'

" Onedark
"let g:onedark_termcolors=256

" Enfocado
let g:enfocado_style = 'neon' "nature | neon

" Set Theme
colorscheme enfocado
