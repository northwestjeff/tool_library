

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

function doAdd() {

}
