$(function(){
                $("#img1").click(function(){
                    var width = $(this).width();
                    if(width==100)
                    {
                        $(this).width(400);
                        $(this).height(400);
                    }
                    else
                    {
                        $(this).width(100);
                        $(this).height(100);
                    }
                });
            });