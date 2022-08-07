let mapleader = ","

" fzf
noremap <leader>f :Files<cr>

" coc
noremap <leader>s :CocSearch 
noremap <silent> gd <Plug>(coc-definition)
noremap <silent> gi <Plug>(coc-implementation)

let g:coc_global_extensions = ['coc-tsserver']

" NERDTree
noremap <leader>d :NERDTree<cr>
noremap <leader>dc :NERDTreeClose<cr>

" Emmet
noremap <leader>! :Emmet !<cr>
noremap <leader>e :Emmet

" Prettier
noremap <leader>p :Prettier<cr>

" Comment
