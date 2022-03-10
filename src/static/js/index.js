$(document).ready( () => {

    $('.send-message').click( async () => {
        $('img').css('display', 'none');
        $('#gif').css('display', 'block');

        const message = $('#message').val();
        const response = await sendMessage(message).catch( err => err);

        if (typeof response != 'number') {
            alert('Deu ruim na requisição')
            return;
        }

        await sleep(2);
        displayAnalysisIcon(response)
    })
})

async function sendMessage(message) {
    return new Promise( (reject, resolve) => {
        $.ajax({
            method: 'POST',
            url: '/api/sentence/analyse',
            data: JSON.stringify({
                sentence: message
            }),
            success: function(response) {
                resolve(response.data)
            },
            error: function(err) {
                console.log(err)
                reject(null)
            }
        })
    })
}

async function sleep(seconds) {
    return new Promise( resolve => {
        setTimeout( () => {
            resolve()
        }, seconds * 1000)
    })
}

function displayAnalysisIcon(analysis) {
    if (analysis) {
        $('#gif').css('display', 'none');
        $('#happy-img').css('display', 'block')
    }

    if (!analysis) {
        $('#gif').css('display', 'none');
        $('#sad-img').css('display', 'block')
    }
}