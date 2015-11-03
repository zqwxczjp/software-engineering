var ImgIputHandler={     
    facePath:[     
        {faceName:"΢Ц",facePath:"0_΢Ц.gif"},     
        {faceName:"Ʋ��",facePath:"1_Ʋ��.gif"},     
        {faceName:"ɫ",facePath:"2_ɫ.gif"},     
        {faceName:"����",facePath:"3_����.gif"},     
        {faceName:"����",facePath:"4_����.gif"},     
        {faceName:"����",facePath:"5_����.gif"},     
        {faceName:"����",facePath:"6_����.gif"},     
        {faceName:"����",facePath:"7_����.gif"},     
        {faceName:"���",facePath:"9_���.gif"},     
        {faceName:"����",facePath:"10_����.gif"},     
        {faceName:"��ŭ",facePath:"11_��ŭ.gif"},     
        {faceName:"��Ƥ",facePath:"12_��Ƥ.gif"},     
        {faceName:"����",facePath:"13_����.gif"},     
        {faceName:"����",facePath:"14_����.gif"},     
        {faceName:"�ѹ�",facePath:"15_�ѹ�.gif"},     
        {faceName:"��",facePath:"16_��.gif"},     
        {faceName:"�亹",facePath:"17_�亹.gif"},     
        {faceName:"ץ��",facePath:"18_ץ��.gif"},     
        {faceName:"��",facePath:"19_��.gif"},     
        {faceName:"͵Ц",facePath:"20_͵Ц.gif"},     
        {faceName:"�ɰ�",facePath:"21_�ɰ�.gif"},     
        {faceName:"����",facePath:"22_����.gif"},     
        {faceName:"����",facePath:"23_����.gif"},     
        {faceName:"����",facePath:"24_����.gif"},     
        {faceName:"��",facePath:"25_��.gif"},     
        {faceName:"����",facePath:"26_����.gif"},     
        {faceName:"����",facePath:"27_����.gif"},     
        {faceName:"��Ц",facePath:"28_��Ц.gif"},     
        {faceName:"���",facePath:"29_���.gif"},     
        {faceName:"�ܶ�",facePath:"30_�ܶ�.gif"},     
        {faceName:"����",facePath:"31_����.gif"},     
        {faceName:"����",facePath:"32_����.gif"},     
        {faceName:"��",facePath:"33_��.gif"},     
        {faceName:"��",facePath:"34_��.gif"},     
        {faceName:"��ĥ",facePath:"35_��ĥ.gif"},     
        {faceName:"˥",facePath:"36_˥.gif"},     
        {faceName:"����",facePath:"37_����.gif"},     
        {faceName:"�ô�",facePath:"38_�ô�.gif"},     
        {faceName:"�ټ�",facePath:"39_�ټ�.gif"},     
        {faceName:"����",facePath:"40_����.gif"},     
             
        {faceName:"�ٱ�",facePath:"41_�ٱ�.gif"},     
        {faceName:"����",facePath:"42_����.gif"},     
        {faceName:"�ܴ���",facePath:"43_�ܴ���.gif"},     
        {faceName:"��Ц",facePath:"44_��Ц.gif"},     
        {faceName:"��ߺ�",facePath:"45_��ߺ�.gif"},     
        {faceName:"�Һߺ�",facePath:"46_�Һߺ�.gif"},     
        {faceName:"��Ƿ",facePath:"47_��Ƿ.gif"},     
        {faceName:"����",facePath:"48_����.gif"},     
        {faceName:"ί��",facePath:"49_ί��.gif"},     
        {faceName:"�����",facePath:"50_�����.gif"},     
        {faceName:"����",facePath:"51_����.gif"},     
        {faceName:"����",facePath:"52_����.gif"},     
        {faceName:"��",facePath:"53_��.gif"},     
        {faceName:"����",facePath:"54_����.gif"},     
        {faceName:"�˵�",facePath:"55_�˵�.gif"},     
        {faceName:"����",facePath:"56_����.gif"},     
        {faceName:"ơ��",facePath:"57_ơ��.gif"},     
        {faceName:"����",facePath:"58_����.gif"},     
        {faceName:"ƹ��",facePath:"59_ƹ��.gif"},     
        {faceName:"ӵ��",facePath:"78_ӵ��.gif"},     
        {faceName:"����",facePath:"81_����.gif"},     
        {faceName:"�����Ц",facePath:"�����Ц.gif"},     
        {faceName:"������",facePath:"������.gif"}     
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