function modal_open_by_id(id) {
    document.getElementById(id).classList.remove('hidden');
}

function modal_close_by_id(id) {
    document.getElementById(id).classList.add('hidden');
}

function change_lang(lang) {
    fetch(`/lang/${lang}`, {
        method: 'POST',
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/';
        } else {
            console.error('Failed to change language');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
