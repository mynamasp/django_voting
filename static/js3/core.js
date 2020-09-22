$(document).ready(function () {
          $("#group1").click(function(){
            $("#next").attr("disabled", false);
            $("#tab2").removeClass("inactiveLink");
          });
           $("#group2").click(function(){
            $("#next2").attr("disabled", false);
            $("#tab3").removeClass("inactiveLink");
          });
          $("#group3").click(function(){
            $("#next3").attr("disabled", false);
            $("#tab4").removeClass("inactiveLink");
          });
          $("#group4").click(function(){
            $("#next4").attr("disabled", false);
          });
    });