/**
 *
 * Created by alberick on 1/10/15.
 */

$(function(){
    console.log("whee!")

    //event handler
    $("#btn-click").click(function(){
        if ($('input').val() !== '') {
            // grab the value from the input box after the click
            var input = $('input').val()
            // display the value within the browser console
            console.log(input)
            // add the value to the dom
            $('ol').append('<li><a href="">x</a>' + input + '</li>');
        }
        $('input').val('');
    });

});