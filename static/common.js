$(document).ready(function () {

    $('#form').on('submit',function () {
        var test = $(this).find('input').val();
        console.log(test);
    });

});