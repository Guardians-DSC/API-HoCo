#!/bin/bash

create_html_doc() {
	local base_path=$(pwd)

	local doc_path="$base_path/api.md"
	local markHTML_path="$base_path/MarkHTML"

	local output_path="$base_path/api_hoco/templates/index.html"

	local html_title="HoCo-Documentation"

	local css_path="/static/style.css"

	if [ ! -d $markHTML_path ]
	then
		git clone https://github.com/RodrigoEC/MarkHTML
	fi

	cd MarkHTML


	bash MarkHTML.sh $doc_path $output_path $html_title $css_path

	cd ..
	echo "Transição da doc finalizada!"
}

create_html_doc
