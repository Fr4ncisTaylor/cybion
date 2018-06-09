# -*- coding:utf-8 -*-
from . import configs as c

class cor:

	prefix = '\033['
	nocolor = prefix + '0m'
	b  = c.b
	r  = c.r
	g  = c.g
	y  = c.y
	bl = c.bl
	m  = c.m
	c  = c.c
	w  = c.w
	PFM = c.PFM
	bold      = c.BOLD
	dark      = c.dark
	underline = c.UNDERLINE
	negative  = c.NEGATIVE
	hide      = c.HIDE

	color     = c.COLOR
	bg_color  = c.BG_COLOR
	light     = c.LIGHT
	bg_light  = c.BG_LIGHT

	black   = prefix + str(color + b) + PFM
	red     = prefix + str(color + r) + PFM
	green   = prefix + str(color + g) + PFM
	yellow  = prefix + str(color + y) + PFM
	blue    = prefix + str(color + bl) + PFM
	magenta = prefix + str(color + m) + PFM
	cyan    = prefix + str(color + c) + PFM
	white   = prefix + str(color + w) + PFM

	lg_black   = prefix + str(light + b) + PFM
	lg_red     = prefix + str(light + r) + PFM
	lg_green   = prefix + str(light + g) + PFM
	lg_yellow  = prefix + str(light + y) + PFM
	lg_blue    = prefix + str(light + bl) + PFM
	lg_magenta = prefix + str(light + m) + PFM
	lg_cyan    = prefix + str(light + c) + PFM
	lg_white   = prefix + str(light + w) + PFM

	bg_black   = prefix + str(bg_color + b) + PFM
	bg_red     = prefix + str(bg_color + r) + PFM
	bg_green   = prefix + str(bg_color + g) + PFM
	bg_yellow  = prefix + str(bg_color + y) + PFM
	bg_blue    = prefix + str(bg_color + bl) + PFM
	bg_magenta = prefix + str(bg_color + m) + PFM
	bg_cyan    = prefix + str(bg_color + c) + PFM
	bg_white   = prefix + str(bg_color + w) + PFM

	bg_lg_black   = prefix + str(bg_light + b) + PFM
	bg_lg_red     = prefix + str(bg_light + r) + PFM
	bg_lg_green   = prefix + str(bg_light + g) + PFM
	bg_lg_yellow  = prefix + str(bg_light + y) + PFM
	bg_lg_blue    = prefix + str(bg_light + bl) + PFM
	bg_lg_magenta = prefix + str(bg_light + m) + PFM
	bg_lg_cyan    = prefix + str(bg_light + c) + PFM
	bg_lg_white   = prefix + str(bg_light + w) + PFM

	bold_black   = prefix + str(bold) + ';' + str(color + b) + PFM
	bold_red     = prefix + str(bold) + ';' + str(color + r) + PFM
	bold_green   = prefix + str(bold) + ';' + str(color + g) + PFM
	bold_yellow  = prefix + str(bold) + ';' + str(color + y) + PFM
	bold_blue    = prefix + str(bold) + ';' + str(color + bl) + PFM
	bold_magenta = prefix + str(bold) + ';' + str(color + m) + PFM
	bold_cyan    = prefix + str(bold) + ';' + str(color + c) + PFM
	bold_white   = prefix + str(bold) + ';' + str(color + w) + PFM

	lg_bold_black   = prefix + str(bold) + ';' + str(light + b) + PFM
	lg_bold_red     = prefix + str(bold) + ';' + str(light + r) + PFM
	lg_bold_green   = prefix + str(bold) + ';' + str(light + g) + PFM
	lg_bold_yellow  = prefix + str(bold) + ';' + str(light + y) + PFM
	lg_bold_blue    = prefix + str(bold) + ';' + str(light + bl) + PFM
	lg_bold_magenta = prefix + str(bold) + ';' + str(light + m) + PFM
	lg_bold_cyan    = prefix + str(bold) + ';' + str(light + c) + PFM
	lg_bold_white   = prefix + str(bold) + ';' + str(light + w) + PFM


	bg_bold_black   = prefix + str(bold) + ';' + str(bg_color + b) + PFM
	bg_bold_red     = prefix + str(bold) + ';' + str(bg_color + r) + PFM
	bg_bold_green   = prefix + str(bold) + ';' + str(bg_color + g) + PFM
	bg_bold_yellow  = prefix + str(bold) + ';' + str(bg_color + y) + PFM
	bg_bold_blue    = prefix + str(bold) + ';' + str(bg_color + bl) + PFM
	bg_bold_magenta = prefix + str(bold) + ';' + str(bg_color + m) + PFM
	bg_bold_cyan    = prefix + str(bold) + ';' + str(bg_color + c) + PFM
	bg_bold_white   = prefix + str(bold) + ';' + str(bg_color + w) + PFM


	bg_lg_bold_black   = prefix + str(bold) + ';' + str(bg_light + b) + PFM
	bg_lg_bold_red     = prefix + str(bold) + ';' + str(bg_light + r) + PFM
	bg_lg_bold_green   = prefix + str(bold) + ';' + str(bg_light + g) + PFM
	bg_lg_bold_yellow  = prefix + str(bold) + ';' + str(bg_light + y) + PFM
	bg_lg_bold_blue    = prefix + str(bold) + ';' + str(bg_light + bl) + PFM
	bg_lg_bold_magenta = prefix + str(bold) + ';' + str(bg_light + m) + PFM
	bg_lg_bold_cyan    = prefix + str(bold) + ';' + str(bg_light + c) + PFM
	bg_lg_bold_white   = prefix + str(bold) + ';' + str(bg_light + w) + PFM


	dark_black   = prefix + str(dark) + ';' + str(color + b) + PFM
	dark_red     = prefix + str(dark) + ';' + str(color + r) + PFM
	dark_green   = prefix + str(dark) + ';' + str(color + g) + PFM
	dark_yellow  = prefix + str(dark) + ';' + str(color + y) + PFM
	dark_blue    = prefix + str(dark) + ';' + str(color + bl) + PFM
	dark_magenta = prefix + str(dark) + ';' + str(color + m) + PFM
	dark_cyan    = prefix + str(dark) + ';' + str(color + c) + PFM
	dark_white   = prefix + str(dark) + ';' + str(color + w) + PFM


	lg_dark_black   = prefix + str(dark) + ';' + str(light + b) + PFM
	lg_dark_red     = prefix + str(dark) + ';' + str(light + r) + PFM
	lg_dark_green   = prefix + str(dark) + ';' + str(light + g) + PFM
	lg_dark_yellow  = prefix + str(dark) + ';' + str(light + y) + PFM
	lg_dark_blue    = prefix + str(dark) + ';' + str(light + bl) + PFM
	lg_dark_magenta = prefix + str(dark) + ';' + str(light + m) + PFM
	lg_dark_cyan    = prefix + str(dark) + ';' + str(light + c) + PFM
	lg_dark_white   = prefix + str(dark) + ';' + str(light + w) + PFM


	bg_dark_black   = prefix + str(dark) + ';' + str(bg_color + b) + PFM
	bg_dark_red     = prefix + str(dark) + ';' + str(bg_color + r) + PFM
	bg_dark_green   = prefix + str(dark) + ';' + str(bg_color + g) + PFM
	bg_dark_yellow  = prefix + str(dark) + ';' + str(bg_color + y) + PFM
	bg_dark_blue    = prefix + str(dark) + ';' + str(bg_color + bl) + PFM
	bg_dark_magenta = prefix + str(dark) + ';' + str(bg_color + m) + PFM
	bg_dark_cyan    = prefix + str(dark) + ';' + str(bg_color + c) + PFM
	bg_dark_white   = prefix + str(dark) + ';' + str(bg_color + w) + PFM


	bg_lg_dark_black   = prefix + str(dark) + ';' + str(bg_light + b) + PFM
	bg_lg_dark_red     = prefix + str(dark) + ';' + str(bg_light + r) + PFM
	bg_lg_dark_green   = prefix + str(dark) + ';' + str(bg_light + g) + PFM
	bg_lg_dark_yellow  = prefix + str(dark) + ';' + str(bg_light + y) + PFM
	bg_lg_dark_blue    = prefix + str(dark) + ';' + str(bg_light + bl) + PFM
	bg_lg_dark_magenta = prefix + str(dark) + ';' + str(bg_light + m) + PFM
	bg_lg_dark_cyan    = prefix + str(dark) + ';' + str(bg_light + c) + PFM
	bg_lg_dark_white   = prefix + str(dark) + ';' + str(bg_light + w) + PFM


	underline_black   = prefix + str(underline) + ';' + str(color + b) + PFM
	underline_red     = prefix + str(underline) + ';' + str(color + r) + PFM
	underline_green   = prefix + str(underline) + ';' + str(color + g) + PFM
	underline_yellow  = prefix + str(underline) + ';' + str(color + y) + PFM
	underline_blue    = prefix + str(underline) + ';' + str(color + bl) + PFM
	underline_magenta = prefix + str(underline) + ';' + str(color + m) + PFM
	underline_cyan    = prefix + str(underline) + ';' + str(color + c) + PFM
	underline_white   = prefix + str(underline) + ';' + str(color + w) + PFM


	lg_underline_black   = prefix + str(underline) + ';' + str(light + b) + PFM
	lg_underline_red     = prefix + str(underline) + ';' + str(light + r) + PFM
	lg_underline_green   = prefix + str(underline) + ';' + str(light + g) + PFM
	lg_underline_yellow  = prefix + str(underline) + ';' + str(light + y) + PFM
	lg_underline_blue    = prefix + str(underline) + ';' + str(light + bl) + PFM
	lg_underline_magenta = prefix + str(underline) + ';' + str(light + m) + PFM
	lg_underline_cyan    = prefix + str(underline) + ';' + str(light + c) + PFM
	lg_underline_white   = prefix + str(underline) + ';' + str(light + w) + PFM


	bg_underline_black   = prefix + str(underline) + ';' + str(bg_color + b) + PFM
	bg_underline_red     = prefix + str(underline) + ';' + str(bg_color + r) + PFM
	bg_underline_green   = prefix + str(underline) + ';' + str(bg_color + g) + PFM
	bg_underline_yellow  = prefix + str(underline) + ';' + str(bg_color + y) + PFM
	bg_underline_blue    = prefix + str(underline) + ';' + str(bg_color + bl) + PFM
	bg_underline_magenta = prefix + str(underline) + ';' + str(bg_color + m) + PFM
	bg_underline_cyan    = prefix + str(underline) + ';' + str(bg_color + c) + PFM
	bg_underline_white   = prefix + str(underline) + ';' + str(bg_color + w) + PFM


	bg_lg_underline_black   = prefix + str(underline) + ';' + str(bg_light + b) + PFM
	bg_lg_underline_red     = prefix + str(underline) + ';' + str(bg_light + r) + PFM
	bg_lg_underline_green   = prefix + str(underline) + ';' + str(bg_light + g) + PFM
	bg_lg_underline_yellow  = prefix + str(underline) + ';' + str(bg_light + y) + PFM
	bg_lg_underline_blue    = prefix + str(underline) + ';' + str(bg_light + bl) + PFM
	bg_lg_underline_magenta = prefix + str(underline) + ';' + str(bg_light + m) + PFM
	bg_lg_underline_cyan    = prefix + str(underline) + ';' + str(bg_light + c) + PFM
	bg_lg_underline_white   = prefix + str(underline) + ';' + str(bg_light + w) + PFM


	negative_black   = prefix + str(negative) + ';' + str(color + b) + PFM
	negative_red     = prefix + str(negative) + ';' + str(color + r) + PFM
	negative_green   = prefix + str(negative) + ';' + str(color + g) + PFM
	negative_yellow  = prefix + str(negative) + ';' + str(color + y) + PFM
	negative_blue    = prefix + str(negative) + ';' + str(color + bl) + PFM
	negative_magenta = prefix + str(negative) + ';' + str(color + m) + PFM
	negative_cyan    = prefix + str(negative) + ';' + str(color + c) + PFM
	negative_white   = prefix + str(negative) + ';' + str(color + w) + PFM


	lg_negative_black   = prefix + str(negative) + ';' + str(light + b) + PFM
	lg_negative_red     = prefix + str(negative) + ';' + str(light + r) + PFM
	lg_negative_green   = prefix + str(negative) + ';' + str(light + g) + PFM
	lg_negative_yellow  = prefix + str(negative) + ';' + str(light + y) + PFM
	lg_negative_blue    = prefix + str(negative) + ';' + str(light + bl) + PFM
	lg_negative_magenta = prefix + str(negative) + ';' + str(light + m) + PFM
	lg_negative_cyan    = prefix + str(negative) + ';' + str(light + c) + PFM
	lg_negative_white   = prefix + str(negative) + ';' + str(light + w) + PFM


	bg_negative_black   = prefix + str(negative) + ';' + str(bg_color + b) + PFM
	bg_negative_red     = prefix + str(negative) + ';' + str(bg_color + r) + PFM
	bg_negative_green   = prefix + str(negative) + ';' + str(bg_color + g) + PFM
	bg_negative_yellow  = prefix + str(negative) + ';' + str(bg_color + y) + PFM
	bg_negative_blue    = prefix + str(negative) + ';' + str(bg_color + bl) + PFM
	bg_negative_magenta = prefix + str(negative) + ';' + str(bg_color + m) + PFM
	bg_negative_cyan    = prefix + str(negative) + ';' + str(bg_color + c) + PFM
	bg_negative_white   = prefix + str(negative) + ';' + str(bg_color + w) + PFM


	bg_lg_negative_black   = prefix + str(negative) + ';' + str(bg_light + b) + PFM
	bg_lg_negative_red     = prefix + str(negative) + ';' + str(bg_light + r) + PFM
	bg_lg_negative_green   = prefix + str(negative) + ';' + str(bg_light + g) + PFM
	bg_lg_negative_yellow  = prefix + str(negative) + ';' + str(bg_light + y) + PFM
	bg_lg_negative_blue    = prefix + str(negative) + ';' + str(bg_light + bl) + PFM
	bg_lg_negative_magenta = prefix + str(negative) + ';' + str(bg_light + m) + PFM
	bg_lg_negative_cyan    = prefix + str(negative) + ';' + str(bg_light + c) + PFM
	bg_lg_negative_white   = prefix + str(negative) + ';' + str(bg_light + w) + PFM


	hide_black   = prefix + str(hide) + ';' + str(color + b) + PFM
	hide_red     = prefix + str(hide) + ';' + str(color + r) + PFM
	hide_green   = prefix + str(hide) + ';' + str(color + g) + PFM
	hide_yellow  = prefix + str(hide) + ';' + str(color + y) + PFM
	hide_blue    = prefix + str(hide) + ';' + str(color + bl) + PFM
	hide_magenta = prefix + str(hide) + ';' + str(color + m) + PFM
	hide_cyan    = prefix + str(hide) + ';' + str(color + c) + PFM
	hide_white   = prefix + str(hide) + ';' + str(color + w) + PFM


	lg_hide_black   = prefix + str(hide) + ';' + str(light + b) + PFM
	lg_hide_red     = prefix + str(hide) + ';' + str(light + r) + PFM
	lg_hide_green   = prefix + str(hide) + ';' + str(light + g) + PFM
	lg_hide_yellow  = prefix + str(hide) + ';' + str(light + y) + PFM
	lg_hide_blue    = prefix + str(hide) + ';' + str(light + bl) + PFM
	lg_hide_magenta = prefix + str(hide) + ';' + str(light + m) + PFM
	lg_hide_cyan    = prefix + str(hide) + ';' + str(light + c) + PFM
	lg_hide_white   = prefix + str(hide) + ';' + str(light + w) + PFM


	bg_hide_black   = prefix + str(hide) + ';' + str(bg_color + b) + PFM
	bg_hide_red     = prefix + str(hide) + ';' + str(bg_color + r) + PFM
	bg_hide_green   = prefix + str(hide) + ';' + str(bg_color + g) + PFM
	bg_hide_yellow  = prefix + str(hide) + ';' + str(bg_color + y) + PFM
	bg_hide_blue    = prefix + str(hide) + ';' + str(bg_color + bl) + PFM
	bg_hide_magenta = prefix + str(hide) + ';' + str(bg_color + m) + PFM
	bg_hide_cyan    = prefix + str(hide) + ';' + str(bg_color + c) + PFM
	bg_hide_white   = prefix + str(hide) + ';' + str(bg_color + w) + PFM


	bg_lg_hide_black   = prefix + str(hide) + ';' + str(bg_light + b) + PFM
	bg_lg_hide_red     = prefix + str(hide) + ';' + str(bg_light + r) + PFM
	bg_lg_hide_green   = prefix + str(hide) + ';' + str(bg_light + g) + PFM
	bg_lg_hide_yellow  = prefix + str(hide) + ';' + str(bg_light + y) + PFM
	bg_lg_hide_blue    = prefix + str(hide) + ';' + str(bg_light + bl) + PFM
	bg_lg_hide_magenta = prefix + str(hide) + ';' + str(bg_light + m) + PFM
	bg_lg_hide_cyan    = prefix + str(hide) + ';' + str(bg_light + c) + PFM
	bg_lg_hide_white   = prefix + str(hide) + ';' + str(bg_light + w) + PFM

