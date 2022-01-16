window.addEventListener('DOMContentLoaded', () => {

})

$(document).ready(function () {
    let preview__file = document.getElementById('preview__file');
    if (preview__file && preview__file.getAttribute('src') && preview__file.getAttribute('src').length !== 0)
        $('#preview__file')
            .show();
    else
        $('#preview__file')
            .hide();
})

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#preview__file')
                .attr('src', e.target.result);
            $('#preview__file')
                .show();
        };
        reader.readAsDataURL(input.files[0]);
    }
}