// static/js/payment.js

document.addEventListener('DOMContentLoaded', () => {
    const buyButton = document.getElementById('buy-button');
    const paymentForm = document.getElementById('payment-form');
    const cardElement = document.getElementById('card-element');
    const submitButton = document.getElementById('submit');
    const paymentResponse = document.getElementById('payment-response');

    if (buyButton) {
        buyButton.addEventListener('click', () => {
            paymentForm.style.display = 'block';
            buyButton.style.display = 'none';
        });
    }

    const stripe = Stripe('{{ STRIPE_TEST_PUBLIC_KEY }}');
    const elements = stripe.elements();
    const card = elements.create('card');
    card.mount('#card-element');

    paymentForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const { paymentMethod, error } = await stripe.createPaymentMethod({
            type: 'card',
            card: card,
        });

        if (error) {
            paymentResponse.textContent = error.message;
        } else {
            const response = await fetch('{% url "create_payment_intent" %}', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}',
                },
                body: JSON.stringify({ payment_method_id: paymentMethod.id }),
            });

            const data = await response.json();

            if (data.error) {
                paymentResponse.textContent = data.error;
            } else {
                const { client_secret } = data;
                const { paymentIntent, error: confirmError } = await stripe.confirmCardPayment(client_secret);

                if (confirmError) {
                    paymentResponse.textContent = confirmError.message;
                } else {
                    paymentResponse.textContent = 'Payment successful!';
                    // You might want to redirect or update the page here
                }
            }
        }
    });
});
// static/js/payment.js

document.addEventListener('DOMContentLoaded', () => {
    const stripe = Stripe('your_test_public_key'); // Replace with your actual public key

    document.querySelectorAll('.btn-primary').forEach(button => {
        button.addEventListener('click', async () => {
            const courseId = button.getAttribute('data-course-id');
            const response = await fetch('/create-payment-intent/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ payment_method_id: courseId }),
            });
            const { client_secret } = await response.json();
            const result = await stripe.confirmCardPayment(client_secret, {
                payment_method: 'your_payment_method_id',
            });
            if (result.error) {
                console.error(result.error.message);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    window.location.href = '/thank_you/';
                }
            }
        });
    });
});
