const deleteButton = document.querySelectorAll('.delete-button');

// for (i=0; i<deleteButton.length; i++){
//     deleteButton[i].addEventListener('click', delete_ajax)
// }


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');


function doDelete(id) {
    $.ajax({
        type: 'POST',
        url: '/delete/',
        data: {
            csrfmiddlewaretoken: csrftoken,
            'tool': id
        },
        dataType: 'json',
        success: function () {
            console.log(id)

        }
    })

}

$(document).on('submit', '#new-tool', function (e) {
    e.preventDefault();
    console.log(e);
    $.ajax({
        type: 'POST',
        url: '/add/',
        data: {
            csrfmiddlewaretoken: csrftoken,
            tool_id: $('#tool_id').val(),
            description: $('#description').val(),
            parts: $('#parts').val(),
            brand: $('#brand').val(),
            model: $('#model').val()
        }
    })

});


function doAdd(id) {
    $.ajax({
        type: 'POST',
        url: '/add/',
        data: {
            csrfmiddlewaretoken: csrftoken,
            'tool': id
        },
        dataType: 'json',
        success: function () {
            console.log("success")

        }
    })
}

$('.nav-main .dropdown-submenu > a:not(a[href="#"])').on('click', function() {
    self.location = $(this).attr('href');
});
