/**
 *
 * Created by alberick on 1/10/15.
 */

$(function(){
    console.log("whee!")

    //event handler
    $("btn-click").click(function(){
        if ($('input').val() !== '') {
            var input = $('input').val()
            console.log(input)
        }
    })
});
