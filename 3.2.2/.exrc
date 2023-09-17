if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <silent> <C-Tab> =UltiSnips#ListSnippets()
imap <Right> <Nop>
imap <Left> <Nop>
imap <Down> <Nop>
imap <Up> <Nop>
inoremap <C-L> u[s1z=`]au
snoremap <silent>  "_c
xnoremap <silent> 	 :call UltiSnips#SaveLastVisualSelection()gvs
snoremap <silent> 	 :call UltiSnips#ExpandSnippetOrJump()
snoremap  "_c
xmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
nmap gcu <Plug>Commentary<Plug>Commentary
nmap gcc <Plug>CommentaryLine
omap gc <Plug>Commentary
nmap gc <Plug>Commentary
xmap gc <Plug>Commentary
xnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
tnoremap <silent> <Plug>(fzf-normal) 
tnoremap <silent> <Plug>(fzf-insert) i
nnoremap <silent> <Plug>(fzf-normal) <Nop>
nnoremap <silent> <Plug>(fzf-insert) i
snoremap <C-R> "_c
snoremap <silent> <C-H> "_c
snoremap <silent> <Del> "_c
snoremap <silent> <BS> "_c
snoremap <silent> <C-Tab> :call UltiSnips#ListSnippets()
nmap <silent> <Plug>CommentaryUndo :echoerr "Change your <Plug>CommentaryUndo map to <Plug>Commentary<Plug>Commentary"
map <Right> <Nop>
map <Left> <Nop>
map <Down> <Nop>
map <Up> <Nop>
inoremap <silent> 	 =UltiSnips#ExpandSnippetOrJump()
inoremap  u[s1z=`]au
inoremap jj 
let &cpo=s:cpo_save
unlet s:cpo_save
set backspace=indent,eol,start
set backupdir=~/.cache/vim/backup//
set directory=~/.cache/vim/swap//
set expandtab
set exrc
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=en
set ruler
set runtimepath=~/.vim,~/.vim/bundle/Vundle.vim,~/.vim/bundle/nerdtree,~/.vim/bundle/vim-commentary,~/.vim/bundle/vimtex,~/.vim/bundle/ultisnips,~/.vim/bundle/rainbow_csv,/usr/share/vim/vimfiles,/usr/share/vim/vim90,/usr/share/vim/vimfiles/after,~/.vim/after,~/.vim/bundle/Vundle.vim,~/.vim/bundle/Vundle.vim/after,~/.vim/bundle/nerdtree/after,~/.vim/bundle/vim-commentary/after,~/.vim/bundle/vimtex/after,~/.vim/bundle/ultisnips/after,~/.vim/bundle/rainbow_csv/after
set secure
set shiftwidth=4
set smarttab
set spelllang=en_us,ru_ru
set suffixes=.bak,~,.o,.info,.swp,.aux,.bbl,.blg,.brf,.cb,.dvi,.idx,.ilg,.ind,.inx,.jpg,.log,.out,.png,.toc,.sty,.cls,.fdb_latexmk,.fls,.pdf,.synctex.gz
set tabstop=4
set termguicolors
set undodir=~/.cache/vim/undo//
set window=73
" vim: set ft=vim :
