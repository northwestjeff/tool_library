// const deleteButton = document.querySelectorAll('.delete-button');


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

function deleteTool(e) {
    console.log(e);
    $.ajax({
        type: 'POST',
        url: '/delete/',
        data: {
            csrfmiddlewaretoken: csrftoken,
            tool_id: e
        },
        success: function () {

            if (!alert(e + ': Tool Deleted')) {
                window.location.reload();
            }
        }
    })
}

$('#check-out-tool-to-user-form').submit(function (e) {
    /*
    Collects the User ID and the Tool ID and passes them to a views.py function
    that adds the Tool to the User account and marks the tool as unavailable
     */
    e.preventDefault();
    // const submitButton = $('#check-out-submit-button');
    const borrower_id = $('#chooseBorrower').val();
    const tool_id = $('div.card-body')[0].id;
    // console.log(borrower_id);
    // console.log(tool_id);
    $.ajax({
        type: 'POST',
        url: '/checkout/',
        data: {
            csrfmiddlewaretoken: csrftoken,
            tool_id: tool_id,
            user: borrower_id
        },
        success: function () {
            // location.reload()
            location.href = '/tools/'
        },
        error: function () {
            alert("Checkout fail")
        }
    })
});


$('#check-out-btn').click(function () {
    const formElement = $('#check-out-tool-to-user-form')[0].style;
    if (formElement.display === 'none') {
        formElement.display = 'block'
    } else {
        formElement.display = 'none'
    }
});


$('#tool-page-return-tool-btn').click(function (e) {
    const borrower_id = $('h6.card-text')[0].id;
    const tool_id = $('div.card-body')[0].id;
    console.log(tool_id);
    console.log(borrower_id);
    $.ajax({
        type: 'POST',
        url: '/returntool/',
        data: {
            csrfmiddlewaretoken: csrftoken,
            tool_id: tool_id,
            borrower_id: borrower_id
        },
        success: function () {
            location.reload()
        },
        error: function () {
            alert("unable to return");
            location.reload()

        }
    })
});

$('#user-page-return-tool-btn').click(function (e) {
    const borrower_id = $('h3.card-title')[0].id;
    const tool_id = this.parentElement.parentElement.id;
    // console.log(tool_id);
    // console.log(borrower_id);
    $.ajax({
        type: 'POST',
        url: '/returntool/',
        data: {
            csrfmiddlewaretoken: csrftoken,
            tool_id: tool_id,
            borrower_id: borrower_id
        },
        success: function (data) {
            // if (data.success === true) {
            //     setTimeout(function () {
            //         location.reload();
            //     }, 2000);
            location.reload()
            // }
        },
        error: function (data) {
            if (data.success === false) {
                setTimeout(function () {
                    location.reload();
                }, 2000);
            }
        }
    })
});

// success: function (data) {
//     if (data.success == true) { // if true (1)
//         setTimeout(function () {// wait for 5 secs(2)
//             location.reload(); // then reload the page.(3)
//         }, 5000);
//     }
// }

// function editTool(e) {
//     console.log(e)
//     $.ajax({
//         type: 'POST',
//         url: '/toolupdate/',
//         data: {
//             csrfmiddlewaretoken: csrftoken,
//             tool_id: e
//         },
//         success: function () {
//
//             // if (!alert(e + ': Tool Deleted')) {
//             //     window.location.reload();
//             }
//
//     })
//     // window.location.href = 'http://localhost:8001/toolupdate.html';
// }

$('#new-user').submit(function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/newuser/',
        data: {
            csrfmiddlewaretoken: csrftoken,
            first_name: $('#first_name').val(),
            last_name: $('#last_name').val(),
            email: $('#email').val(),
            username: $('#username').val(),
            password: $('#password').val(),
            zip: $('#zip').val(),
        },
        success: function (e) {
            console.log("success")
        }
    })
});


// NEW TOOL
$('#new-tool').submit(function (e) {
    e.preventDefault();
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
        },
        success: function (e) {
            // if (!alert(e + ': SUCCESS tool added to tool shelf')) {
            // window.location.reload();
            // }
            alert("Tool created.")
            location.reload()
        },
        error: function (e) {
            console.log(e);
            // if (!alert(e + ': FAIL tool added to tool shelf')) {
            //     window.location.reload();
            // }
        }
    })

});


// UPDATE TOOL
$('#update-tool').submit(function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/update/',
        data: {
            csrfmiddlewaretoken: csrftoken,
            tool_id: $('h3')[0].id,
            description: description.value,
            parts: parts.value,
            brand: brand.value,
            model: model.value,
        },
        success: function (data) {
            alert("tool updated " + data)
        },
        error: function (xhr, status) {
            alert('ajax error = ' + xhr.statusText)
        }
    })
});


$('.nav-main .dropdown-submenu > a:not(a[href="#"])').on('click', function () {
    self.location = $(this).attr('href');
});


