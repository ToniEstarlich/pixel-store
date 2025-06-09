function increaseQty(button) {
    const input = button.closest('.input-group').querySelector('input[type="number"]');
    input.stepUp();
}

function decreaseQty(button) {
    const input = button.closest('.input-group').querySelector('input[type="number"]');
    if (parseInt(input.value) > 1) {
        input.stepDown();
    }
}
