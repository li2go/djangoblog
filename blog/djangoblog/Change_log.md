#"""
##Paginator类方法说明

######  Paginator(models,cut_number) >>> 把MODELS，以CUT_NUMBER为单位进行分割，
#####models=6  self=Paginator(models,2) >>> 一共6条数据，以2位单位 ,分得6/2=3 页
#####self.num_pages  >>> 返回页数  这里=3

#####self.has_next() >>> 是否有下一页 返回布尔值   TRUE OR FALSE
	 
#####self.has_previous() >>> 同上，是否有前一页 
	
#####self.has_other_pages() >>> 是否有其他页 返回布尔值，这个基本不用
	  
#####self.next_page_number() >>> 返回下一页的值   值为INT类型  
	 
#####self.previous_page_number() >>> 返回前一页的值  值为INT类型

#"""
