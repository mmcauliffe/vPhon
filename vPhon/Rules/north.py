﻿#coding: utf-8

onsets = { 'b' : 'b', 't' : 't', 'th' : 'tʰ', 'đ' : 'd', 'ch' : 'c', 
				'kh' : 'x', 'g' : 'ɣ', 'l' : 'l', 'm' : 'm', 'n': 'n', 
				'ngh': 'ŋ', 'nh' : 'ɲ', 'ng' : 'ŋ', 'ph' : 'f', 'v' : 'v', 
				'x' : 's', 'd' : 'z', 'h' : 'h', 'p' : 'p', 'q' : 'kw',
				'gi' : 'z', 'tr' : 'c', 'k' : 'k', 'c' : 'k', 'gh' : 'ɣ', 
				'r' : 'z', 's' : 's', 'gi': 'z'}
				
			  
nuclei = { 'a' : 'a', 'á' : 'a', 'à' : 'a', 'ả' : 'a', 'ã' : 'a', 'ạ' : 'a', 
				'â' : 'ɤ̆', 'ấ' : 'ɤ̆', 'ầ' : 'ɤ̆', 'ẩ' : 'ɤ̆', 'ẫ' : 'ɤ̆', 'ậ' : 'ɤ̆',
				'ă' : 'ă', 'ắ' : 'ă', 'ằ' : 'ă', 'ẳ' : 'ă', 'ẵ' : 'ă', 'ặ' : 'ă',
				'e' : 'ɛ', 'é' : 'ɛ', 'è' : 'ɛ', 'ẻ' : 'ɛ', 'ẽ' : 'ɛ', 'ẹ' : 'ɛ',
				'ê' : 'e', 'ế' : 'e', 'ề' : 'e', 'ể' : 'e', 'ễ' : 'e', 'ệ' : 'e',
				'i' : 'i', 'í' : 'i', 'ì' : 'i', 'ỉ' : 'i', 'ĩ' : 'i', 'ị' : 'i',
				'o' : 'ɔ', 'ó' : 'ɔ', 'ò' : 'ɔ', 'ỏ' : 'ɔ', 'õ' : 'ɔ', 'ọ' : 'ɔ',
				'ô' : 'o', 'ố' : 'o', 'ồ' : 'o', 'ổ' : 'o', 'ỗ' : 'o', 'ộ' : 'o',
				'ơ' : 'ɤ', 'ớ' : 'ɤ', 'ờ' : 'ɤ', 'ở' : 'ɤ', 'ỡ' : 'ɤ', 'ợ' : 'ɤ',
				'' : '', 'ú' : '', 'ù' : '', 'ủ' : '', 'ũ' : '', 'ụ' : '',
				'ư' : 'ɯ', 'ứ' : 'ɯ', 'ừ' : 'ɯ', 'ử' : 'ɯ', 'ữ' : 'ɯ', 'ự' : 'ɯ',
				'y' : 'i', 'ý' : 'i', 'ỳ' : 'i', 'ỷ' : 'i', 'ỹ' : 'i', 'ỵ' : 'i',
				
				'eo' : 'eo', 'éo' : 'eo', 'èo' : 'eo', 'ẻo' : 'eo', 'ẽo': 'eo', 'ẹo' : 'eo',
				'ê' : 'ɛ', 'ế' : 'ɛ', 'ề' : 'ɛ', 'ể' : 'ɛ', 'ễ': 'ɛ', 'ệ' : 'ɛ',
				'ia' : 'iə', 'ía' : 'iə', 'ìa' : 'iə', 'ỉa' : 'iə', 'ĩa' : 'iə', 'ịa' : 'iə',
				'ia' : 'iə', 'iá' : 'iə', 'ià' : 'iə', 'iả' : 'iə', 'iã' : 'iə', 'iạ' : 'iə',
				'iê' : 'iə', 'iế' : 'iə', 'iề' : 'iə', 'iể' : 'iə', 'iễ' : 'iə', 'iệ' : 'iə',
				'oo' : 'ɔ', 'óo' : 'ɔ', 'òo' : 'ɔ', 'ỏo' : 'ɔ', 'õo' : 'ɔ', 'ọo' : 'ɔ',
				'oo' : 'ɔ', 'oó' : 'ɔ', 'oò' : 'ɔ', 'oỏ' : 'ɔ', 'oõ' : 'ɔ', 'oọ' : 'ɔ',
				'ôô' : 'o', 'ốô' : 'o', 'ồô' : 'o', 'ổô' : 'o', 'ỗô' : 'o', 'ộô' : 'o',				                 'ôô' : 'o', 'ôố' : 'o', 'ôồ' : 'o', 'ôổ' : 'o', 'ôỗ' : 'o', 'ôộ' : 'o',				                  'ua' : 'uə', 'úa' : 'uə', 'ùa' : 'uə', 'ủa' : 'uə', 'ũa' : 'uə', 'ụa' : 'uə',
				'uô' : 'uə', 'uố' : 'uə', 'uồ' : 'uə', 'uổ' : 'uə', 'uỗ' : 'uə', 'uộ' : 'uə',
				'ưa' : 'ɯə', 'ứa' : 'ɯə', 'ừa' : 'ɯə', 'ửa' : 'ɯə', 'ữa' : 'ɯə', 'ựa' : 'ɯə',
				'ươ' : 'ɯə', 'ướ' : 'ɯə', 'ườ' : 'ɯə', 'ưở' : 'ɯə', 'ưỡ' : 'ɯə', 'ượ' : 'ɯə',
				'yê' : 'iɛ', 'yế' : 'iɛ', 'yề' : 'iɛ', 'yể' : 'iɛ', 'yễ' : 'iɛ', 'yệ' : 'iɛ', 
                                'uơ' : 'uə',  'uở' : 'uə', 'uờ': 'uə', 'uở' : 'uə', 'uỡ' : 'uə', 'uợ' : 'uə',
				}
				         
				         
offglides =  { 'ai' : 'aj', 'ái' : 'aj', 'ài' : 'aj', 'ải' : 'aj', 'ãi' : 'aj', 'ại' : 'aj',
				  'ay' : 'ăj', 'áy' : 'ăj', 'ày' : 'ăj', 'ảy' : 'ăj', 'ãy' : 'ăj', 'ạy' : 'ăj',
				  'ao' : 'aw', 'áo' : 'aw', 'ào' : 'aw', 'ảo' : 'aw', 'ão' : 'aw', 'ạo' : 'aw',
				  'a' : 'ăw', 'á' : 'ăw', 'à' : 'ăw', 'ả' : 'ăw', 'ã' : 'ăw', 'ạ' : 'ăw',
				  'ây' : 'ɤ̆j',  'ấy' : 'ɤ̆j',  'ầy' : 'ɤ̆j', 'ẩy' : 'ɤ̆j', 'ẫy' : 'ɤ̆j', 'ậy' : 'ɤ̆j', 
				  'â' : 'ɤ̆w', 'ấ' : 'ɤ̆w', 'ầ': 'ɤ̆w', 'ẩ' : 'ɤ̆w', 'ẫ' : 'ɤ̆w', 'ậ' : 'ɤ̆w',
				  'eo' : 'ew', 'éo' : 'ew', 'èo' : 'ew', 'ẻo' : 'ew', 'ẽo' : 'ew', 'ẹo' : 'ew',
				  'i' : 'iw', 'í' : 'iw', 'ì' : 'iw', 'ỉ' : 'iw', 'ĩ' : 'iw', 'ị' : 'iw',
				  'oi' : 'ɔj', 'ói' : 'ɔj', 'òi' : 'ɔj', 'ỏi' : 'ɔj', 'õi' : 'ɔj', 'ọi' : 'ɔj',
				  'ôi' : 'oj', 'ối' : 'oj', 'ồi' : 'oj', 'ổi' : 'oj', 'ỗi' : 'oj', 'ội' : 'oj',
				  'ui' : 'uj', 'úi' : 'uj', 'ùi' : 'uj', 'ủi' : 'uj', 'ũi' : 'uj', 'ụi' : 'uj', 
				  'uy' : 'uj', 'úy' : 'uj', 'ùy' : 'uj', 'ủy' : 'uj', 'ũy' : 'uj', 'ụy' : 'uj', 
				  'ơi' : 'ɤj', 'ới' : 'ɤj', 'ời' : 'ɤj', 'ởi' : 'ɤj', 'ỡi' : 'ɤj', 'ợi' : 'ɤj', 
				  'ưi' : 'ɯj', 'ứi' : 'ɯj', 'ừi' : 'ɯj', 'ửi' : 'ɯj', 'ữi' : 'ɯj', 'ựi' : 'ɯj', 
				  'ư' : 'ɯw', 'ứ' : 'ɯw', 'ừ' : 'ɯw', 'ử' : 'ɯw', 'ữ' : 'ɯw', 'ự' : 'ɯw',

				  'iê' : 'iəw', 'iế' : 'iəw', 'iề' : 'iəw', 'iể' : 'iəw', 'iễ' : 'iəw', 'iệ' : 'iəw',
				  'yê' : 'iəw', 'yế' : 'iəw', 'yề' : 'iəw', 'yể' : 'iəw', 'yễ' : 'iəw', 'yệ' : 'iəw', 
				  'uôi' : 'uəj', 'uối' : 'uəj', 'uồi' : 'uəj', 'uổi' : 'uəj', 'uỗi' : 'uəj', 'uội' : 'uəj', 
				  'ươi' : 'ɯəj', 'ưới' : 'ɯəj', 'ười' : 'ɯəj', 'ưởi' : 'ɯəj', 'ưỡi' : 'ɯəj', 'ượi' : 'ɯəj', 
				  'ươ' : 'ɯəw', 'ướ' : 'ɯəw', 'ườ' : 'ɯəw', 'ưở' : 'ɯəw', 'ưỡ' : 'ɯəw', 'ượ' : 'ɯəw'	 
			    }
				
onglides =   { 'oa' : 'a', 'oá' : 'a', 'oà' : 'a', 'oả' : 'a', 'oã' : 'a', 'oạ' : 'a', 
		              'óa' : 'a', 'òa' : 'a', 'ỏa' : 'a', 'õa' : 'a', 'ọa' : 'a', 
			      'oă' : 'ă', 'oắ' : 'ă', 'oằ' : 'ă', 'oẳ' : 'ă', 'oẵ' : 'ă', 'oặ' : 'ă', 	
			      'oe' : 'e', 'oé' : 'e', 'oè' : 'e', 'oẻ' : 'e', 'oẽ' : 'e', 'oẹ' : 'e', 	
			      'oe' : 'e', 'óe' : 'e', 'òe' : 'e', 'ỏe' : 'e', 'õe' : 'e', 'ọe' : 'e', 	
			      'ua' : 'a', 'uá' : 'a', 'uà' : 'a', 'uả' : 'a', 'uã' : 'a', 'uạ' : 'a', 
			      'uă' : 'ă', 'uắ' : 'ă', 'uằ' : 'ă', 'uẳ' : 'ă', 'uẵ' : 'ă', 'uặ' : 'ă', 	
			      'uâ' : 'ɤ̆', 'uấ' : 'ɤ̆', 'uầ' : 'ɤ̆', 'uẩ' : 'ɤ̆', 'uẫ' : 'ɤ̆', 'uậ' : 'ɤ̆', 
			      'ue' : 'ɛ', 'ué' : 'ɛ', 'uè' : 'ɛ', 'uẻ' : 'ɛ', 'uẽ' : 'ɛ', 'uẹ' : 'ɛ', 
			      'uê' : 'e', 'uế' : 'e', 'uề' : 'e', 'uể' : 'e', 'uễ' : 'e', 'uệ' : 'e', 
			      'uơ' : 'ɤ', 'uớ' : 'ɤ', 'uờ' : 'ɤ', 'uở' : 'ɤ', 'uỡ' : 'ɤ', 'uợ' : 'ɤ', 
			      'uy' : 'i', 'uý' : 'i', 'uỳ' : 'i', 'uỷ' : 'i', 'uỹ' : 'i', 'uỵ' : 'i',
		              'uya' : 'iə', 'uyá' : 'iə', 'uyà' : 'iə', 'uyả' : 'iə', 'uyã' : 'iə', 'uyạ' : 'iə', 
				  'uyê' : 'iə', 'uyế' : 'iə', 'uyề' : 'iə', 'uyể' : 'iə', 'uyễ' : 'iə', 'uyệ' : 'iə', 
				  'uy' : 'i', 'uyú' : 'i', 'uyù' : 'i', 'uyủ' : 'i', 'uyũ' : 'i', 'uyụ' : 'i', 
				  'uy' : 'i', 'uý' : 'i', 'uỳ' : 'i', 'uỷ' : 'i', 'uỹ' : 'i', 'uỵ' : 'i',
                  'oen' : 'en', 'oén' : 'en', 'oèn' : 'en', 'oẻn' : 'en', 'oẽn' : 'en', 'oẹn' : 'en', 	
                  'oet' : 'et', 'oét' : 'et', 'oèt' : 'et', 'oẻt' : 'et', 'oẽt' : 'et', 'oẹt' : 'et' 	
				}

onoffglides = { 'oe' : 'ej', 'oé' : 'ej', 'oè' : 'ej', 'oẻ' : 'ej', 'oẽ' : 'ej', 'oẹ' : 'ej', 
				   'oai' : 'aj', 'oái' : 'aj', 'oài' : 'aj', 'oải' : 'aj', 'oãi' : 'aj', 'oại' : 'aj',
				   'oay' : 'ăj', 'oáy' : 'ăj', 'oày' : 'ăj', 'oảy' : 'ăj', 'oãy' : 'ăj', 'oạy' : 'ăj',
				   'oao' : 'aw', 'oáo' : 'aw', 'oào' : 'aw', 'oảo' : 'aw', 'oão' : 'aw', 'oạo' : 'aw',
				   'oeo' : 'ew', 'oéo' : 'ew', 'oèo' : 'ew', 'oẻo' : 'ew', 'oẽo' : 'ew', 'oẹo' : 'ew',
				   'oeo' : 'ew', 'óeo' : 'ew', 'òeo' : 'ew', 'ỏeo' : 'ew', 'õeo' : 'ew', 'ọeo' : 'ew',
				   'ueo' : 'ew', 'uéo' : 'ew', 'uèo' : 'ew', 'uẻo' : 'ew', 'uẽo' : 'ew', 'uẹo' : 'ew',
				   'uai' : 'aj', 'uái' : 'aj', 'uài' : 'aj', 'uải' : 'aj', 'uãi' : 'aj', 'uại' : 'aj',
				   'uay' : 'ăj', 'uáy' : 'ăj', 'uày' : 'ăj', 'uảy' : 'ăj', 'uãy' : 'ăj', 'uạy' : 'ăj',
				   'uây' : 'ɤ̆j', 'uấy' : 'ɤ̆j', 'uầy' : 'ɤ̆j', 'uẩy' : 'ɤ̆j', 'uẫy' : 'ɤ̆j', 'uậy' : 'ɤ̆j'
				 }

codas = { 'p' : 'p', 't' : 't', 'c' : 'k', 'm' : 'm', 'n' : 'n', 'ng' : 'ŋ', 'nh' : 'ɲ', 'ch' : 'k' }
			

#tones   =     { 'a' : 33, 'á' : 24, 'à' : 32, 'ả' : 312, 'ã' : '35g', 'ạ' : '21g', 
#				'â' : 33, 'ấ' : 24, 'ầ' : 32, 'ẩ' : 312, 'ẫ' : '35g', 'ậ' : '21g',
#				'ă' : 33, 'ắ' : 24, 'ằ' : 32, 'ẳ' : 312, 'ẵ' : '35g', 'ặ' : '21g',
#				'e' : 33, 'é' : 24, 'è' : 32, 'ẻ' : 312, 'ẽ' : '35g', 'ẹ' : '21g',
#				'ê' : 33, 'ế' : 24, 'ề' : 32, 'ể' : 312, 'ễ' : '35g', 'ệ' : '21g',
#				'i' : 33, 'í' : 24, 'ì' : 32, 'ỉ' : 312, 'ĩ' : '35g', 'ị' : '21g',
#				'o' : 33, 'ó' : 24, 'ò' : 32, 'ỏ' : 312, 'õ' : '35g', 'ọ' : '21g',
#				'ô' : 33, 'ố' : 24, 'ồ' : 32, 'ổ' : 312, 'ỗ' : '35g', 'ộ' : '21g',
#				'ơ' : 33, 'ớ' : 24, 'ờ' : 32, 'ở' : 312, 'ỡ' : '35g', 'ợ' : '21g',
#				'' : 33, 'ú' : 24, 'ù' : 32, 'ủ' : 312, 'ũ' : '35g', 'ụ' : '21g',
#				'ư' : 33, 'ứ' : 24, 'ừ' : 32, 'ử' : 312, 'ữ' : '35g', 'ự' : '21g',
#				'y' : 33, 'ý' : 24, 'ỳ' : 32, 'ỷ' : 312, 'ỹ' : '35g', 'ỵ' : '21g',
#			  }

tones   =     { 'á' : 24, 'à' : 32, 'ả' : 312, 'ã' : '35g', 'ạ' : '21g', 
				'ấ' : 24, 'ầ' : 32, 'ẩ' : 312, 'ẫ' : '35g', 'ậ' : '21g',
				'ắ' : 24, 'ằ' : 32, 'ẳ' : 312, 'ẵ' : '35g', 'ặ' : '21g',
				'é' : 24, 'è' : 32, 'ẻ' : 312, 'ẽ' : '35g', 'ẹ' : '21g',
				'ế' : 24, 'ề' : 32, 'ể' : 312, 'ễ' : '35g', 'ệ' : '21g',
				'í' : 24, 'ì' : 32, 'ỉ' : 312, 'ĩ' : '35g', 'ị' : '21g',
				'ó' : 24, 'ò' : 32, 'ỏ' : 312, 'õ' : '35g', 'ọ' : '21g',
				'ố' : 24, 'ồ' : 32, 'ổ' : 312, 'ỗ' : '35g', 'ộ' : '21g',
				'ớ' : 24, 'ờ' : 32, 'ở' : 312, 'ỡ' : '35g', 'ợ' : '21g',
				'ú' : 24, 'ù' : 32, 'ủ' : 312, 'ũ' : '35g', 'ụ' : '21g',
				'ứ' : 24, 'ừ' : 32, 'ử' : 312, 'ữ' : '35g', 'ự' : '21g',
				'ý' : 24, 'ỳ' : 32, 'ỷ' : 312, 'ỹ' : '35g', 'ỵ' : '21g',
			  }
# used to use \u02C0 for the unicode raised glottal character

tones_p =     { 'á' : 5, 'à' : 2, 'ả' : 4, 'ã' : 3, 'ạ' : 6, 
				'ấ' : 5, 'ầ' : 2, 'ẩ' : 4, 'ẫ' : 3, 'ậ' : 6,
				'ắ' : 5, 'ằ' : 2, 'ẳ' : 4, 'ẵ' : 3, 'ặ' : 6,
				'é' : 5, 'è' : 2, 'ẻ' : 4, 'ẽ' : 3, 'ẹ' : 6,
				'ế' : 5, 'ề' : 2, 'ể' : 4, 'ễ' : 3, 'ệ' : 6,
				'í' : 5, 'ì' : 2, 'ỉ' : 4, 'ĩ' : 3, 'ị' : 6,
				'ó' : 5, 'ò' : 2, 'ỏ' : 4, 'õ' : 3, 'ọ' : 6,
				'ố' : 5, 'ồ' : 2, 'ổ' : 4, 'ỗ' : 3, 'ộ' : 6,
				'ớ' : 5, 'ờ' : 2, 'ở' : 4, 'ỡ' : 3, 'ợ' : 6,
				'ú' : 5, 'ù' : 2, 'ủ' : 4, 'ũ' : 3, 'ụ' : 6,
				'ứ' : 5, 'ừ' : 2, 'ử' : 4, 'ữ' : 3, 'ự' : 6,
				'ý' : 5, 'ỳ' : 2, 'ỷ' : 4, 'ỹ' : 3, 'ỵ' : 6,
			  }
			  
gi = { 'gi' : 'zi', 'gí': 'zi', 'gì' : 'zi', 'gì' : 'zi', 'gĩ' : 'zi', 'gị' : 'zi'}

qu = {'quy' : 'kwi', 'qúy' : 'kwi', 'qùy' : 'kwi', 'qủy' : 'kwi', 'qũy' : 'kwi', 'qụy' : 'kwi'}

