#!/usr/bin/perl

use feature qw(say);
use Text::Markup::Markdown;

my $html = Text::Markup->new->parse(file => 'menu.md');


open my $fh, ">", "index.html";
print $fh $html;


say $html;
