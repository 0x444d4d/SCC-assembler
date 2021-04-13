" Vim syntax file
" Language: SASM
" Maintainer: David Martin
" Latest Revision: 6/4/2021 d/m/y

if exists("b:current_syntax")
  finish
endif


syn match comment '#.*$'
syn match preproc '^\.code$'
syn keyword preproc use nextgroup=const
syn keyword preproc as
syn keyword opcode noop ret sw lw sa la call or add sub not movsyn 
syn keyword opcode li nextgroup=number,const
syn keyword opaddr jump jz jnz call nextgroup=addrtag,number skipwhite
syn match const '\w\+'
syn match number '\d\+'
syn match addr '[a-zA-Z0-9_-]\+$'
syn match addrtag ':[a-zA-Z0-9_-]\+'
syn match addr 'io(\d\+)'
syn match addr 'data(\d\+)'
syn match addr 'int(\d\+)'
syn match reg 'R\d'

let b:current_syntax = "sasm"
hi def link opcode	Type
hi def link opaddr 	Type
hi def link addr 	Constant
hi def link const 	PreProc
hi def link reg 	Statement
hi def link comment 	Comment
hi def link addrtag 	Statement
hi def link preproc 	PreProc
hi def link number 	Constant
"hi def link opaddr Statement
"hi def link op3Reg Statement

