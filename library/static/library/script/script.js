

const deleteButton = document.querySelectorAll('.delete-button');

for (i=0; i<deleteButton.length; i++){
    deleteButton[i].addEventListener('click', delete_ajax)
}

function delete_ajax() {
        console.log('delete via AJAX')
        var tool = this.val();

        $.ajax({
            type: 'POST',
            url: '/delete',
            data: {
                'tool': tool
            },
            dataType: 'json',
            success: function () {
                tool.delete()

            }
        })
    }

