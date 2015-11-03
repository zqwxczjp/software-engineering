var ImgIputHandler={     
    facePath:[     
        {faceName:"Î¢Ð¦",facePath:"0_Î¢Ð¦.gif"},     
        {faceName:"Æ²×ì",facePath:"1_Æ²×ì.gif"},     
        {faceName:"É«",facePath:"2_É«.gif"},     
        {faceName:"·¢´ô",facePath:"3_·¢´ô.gif"},     
        {faceName:"µÃÒâ",facePath:"4_µÃÒâ.gif"},     
        {faceName:"Á÷Àá",facePath:"5_Á÷Àá.gif"},     
        {faceName:"º¦Ðß",facePath:"6_º¦Ðß.gif"},     
        {faceName:"±Õ×ì",facePath:"7_±Õ×ì.gif"},     
        {faceName:"´ó¿Þ",facePath:"9_´ó¿Þ.gif"},     
        {faceName:"ÞÏÞÎ",facePath:"10_ÞÏÞÎ.gif"},     
        {faceName:"·¢Å­",facePath:"11_·¢Å­.gif"},     
        {faceName:"µ÷Æ¤",facePath:"12_µ÷Æ¤.gif"},     
        {faceName:"ö·ÑÀ",facePath:"13_ö·ÑÀ.gif"},     
        {faceName:"¾ªÑÈ",facePath:"14_¾ªÑÈ.gif"},     
        {faceName:"ÄÑ¹ý",facePath:"15_ÄÑ¹ý.gif"},     
        {faceName:"¿á",facePath:"16_¿á.gif"},     
        {faceName:"Àäº¹",facePath:"17_Àäº¹.gif"},     
        {faceName:"×¥¿ñ",facePath:"18_×¥¿ñ.gif"},     
        {faceName:"ÍÂ",facePath:"19_ÍÂ.gif"},     
        {faceName:"ÍµÐ¦",facePath:"20_ÍµÐ¦.gif"},     
        {faceName:"¿É°®",facePath:"21_¿É°®.gif"},     
        {faceName:"°×ÑÛ",facePath:"22_°×ÑÛ.gif"},     
        {faceName:"°ÁÂý",facePath:"23_°ÁÂý.gif"},     
        {faceName:"¼¢¶ö",facePath:"24_¼¢¶ö.gif"},     
        {faceName:"À§",facePath:"25_À§.gif"},     
        {faceName:"¾ª¿Ö",facePath:"26_¾ª¿Ö.gif"},     
        {faceName:"Á÷º¹",facePath:"27_Á÷º¹.gif"},     
        {faceName:"º©Ð¦",facePath:"28_º©Ð¦.gif"},     
        {faceName:"´ó±ø",facePath:"29_´ó±ø.gif"},     
        {faceName:"·Ü¶·",facePath:"30_·Ü¶·.gif"},     
        {faceName:"ÖäÂî",facePath:"31_ÖäÂî.gif"},     
        {faceName:"ÒÉÎÊ",facePath:"32_ÒÉÎÊ.gif"},     
        {faceName:"Ðê",facePath:"33_Ðê.gif"},     
        {faceName:"ÔÎ",facePath:"34_ÔÎ.gif"},     
        {faceName:"ÕÛÄ¥",facePath:"35_ÕÛÄ¥.gif"},     
        {faceName:"Ë¥",facePath:"36_Ë¥.gif"},     
        {faceName:"÷¼÷Ã",facePath:"37_÷¼÷Ã.gif"},     
        {faceName:"ÇÃ´ò",facePath:"38_ÇÃ´ò.gif"},     
        {faceName:"ÔÙ¼û",facePath:"39_ÔÙ¼û.gif"},     
        {faceName:"²Áº¹",facePath:"40_²Áº¹.gif"},     
             
        {faceName:"¿Ù±Ç",facePath:"41_¿Ù±Ç.gif"},     
        {faceName:"¹ÄÕÆ",facePath:"42_¹ÄÕÆ.gif"},     
        {faceName:"ôÜ´óÁË",facePath:"43_ôÜ´óÁË.gif"},     
        {faceName:"»µÐ¦",facePath:"44_»µÐ¦.gif"},     
        {faceName:"×óºßºß",facePath:"45_×óºßºß.gif"},     
        {faceName:"ÓÒºßºß",facePath:"46_ÓÒºßºß.gif"},     
        {faceName:"¹þÇ·",facePath:"47_¹þÇ·.gif"},     
        {faceName:"±ÉÊÓ",facePath:"48_±ÉÊÓ.gif"},     
        {faceName:"Î¯Çü",facePath:"49_Î¯Çü.gif"},     
        {faceName:"¿ì¿ÞÁË",facePath:"50_¿ì¿ÞÁË.gif"},     
        {faceName:"ÒõÏÕ",facePath:"51_ÒõÏÕ.gif"},     
        {faceName:"Ç×Ç×",facePath:"52_Ç×Ç×.gif"},     
        {faceName:"ÏÅ",facePath:"53_ÏÅ.gif"},     
        {faceName:"¿ÉÁ¯",facePath:"54_¿ÉÁ¯.gif"},     
        {faceName:"²Ëµ¶",facePath:"55_²Ëµ¶.gif"},     
        {faceName:"Î÷¹Ï",facePath:"56_Î÷¹Ï.gif"},     
        {faceName:"Æ¡¾Æ",facePath:"57_Æ¡¾Æ.gif"},     
        {faceName:"ÀºÇò",facePath:"58_ÀºÇò.gif"},     
        {faceName:"Æ¹ÅÒ",facePath:"59_Æ¹ÅÒ.gif"},     
        {faceName:"Óµ±§",facePath:"78_Óµ±§.gif"},     
        {faceName:"ÎÕÊÖ",facePath:"81_ÎÕÊÖ.gif"},     
        {faceName:"µÃÒâµØÐ¦",facePath:"µÃÒâµØÐ¦.gif"},     
        {faceName:"ÌýÒôÀÖ",facePath:"ÌýÒôÀÖ.gif"}     
    ]     
    ,     
    Init:function(){     
        var isShowImg=false;     
        $(".Input_text").focusout(function(){     
            $(this).parent().css("border-color", "#cccccc");     
            $(this).parent().css("box-shadow", "none");     
            $(this).parent().css("-moz-box-shadow", "none");     
            $(this).parent().css("-webkit-box-shadow", "none");     
        });     
        $(".Input_text").focus(function(){     
        $(this).parent().css("border-color", "rgba(19,105,172,.75)");     
        $(this).parent().css("box-shadow", "0 0 3px rgba(19,105,192,.5)");     
        $(this).parent().css("-moz-box-shadow", "0 0 3px rgba(241,39,232,.5)");     
        $(this).parent().css("-webkit-box-shadow", "0 0 3px rgba(19,105,252,3)");     
        });     
        $(".imgBtn").click(function(){     
            if(isShowImg==false){     
                isShowImg=true;     
                $(this).parent().prev().animate({marginTop:"-125px"},300);     
                if($(".faceDiv").children().length==0){     
                    for(var i=0;i<ImgIputHandler.facePath.length;i  ){     
                        $(".faceDiv").append("<img title=\"" ImgIputHandler.facePath[i].faceName "\" src=\"face/" ImgIputHandler.facePath[i].facePath "\" />");     
                    }     
                    $(".faceDiv>img").click(function(){     
                              
                        isShowImg=false;     
                        $(this).parent().animate({marginTop:"0px"},300);     
                        ImgIputHandler.insertAtCursor($(".Input_text")[0],"[" $(this).attr("title") "]");     
                    });     
                }     
            }else{     
                isShowImg=false;     
                $(this).parent().prev().animate({marginTop:"0px"},300);     
            }     
        });     
        $(".postBtn").click(function(){     
            alert($(".Input_text").val());     
        });     
    },     
    insertAtCursor:function(myField, myValue) {     
    if (document.selection) {     
        myField.focus();     
        sel = document.selection.createRange();     
        sel.text = myValue;     
        sel.select();     
    } else if (myField.selectionStart || myField.selectionStart == "0") {     
        var startPos = myField.selectionStart;     
        var endPos = myField.selectionEnd;     
        var restoreTop = myField.scrollTop;     
        myField.value = myField.value.substring(0, startPos)   myValue   myField.value.substring(endPos, myField.value.length);     
        if (restoreTop > 0) {     
            myField.scrollTop = restoreTop;     
        }     
        myField.focus();     
        myField.selectionStart = startPos   myValue.length;     
        myField.selectionEnd = startPos   myValue.length;     
    } else {     
        myField.value  = myValue;     
        myField.focus();     
    }     
}     
}