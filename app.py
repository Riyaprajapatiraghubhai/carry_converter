from flask import Flask, render_template, request

app = Flask(__name__)

# Mock exchange rates dictionary
exchange_rates = {
    'USD': {'EUR': 0.85, 'INR': 83.2},
    'EUR': {'USD': 1.18, 'INR': 97.6},
    'INR': {'USD': 0.012, 'EUR': 0.010}
}

@app.route('/', methods=['GET', 'POST'])
def convert_currency():
    result = None
    currencies = list(exchange_rates.keys())

    if request.method == 'POST':
        try:
            amount = float(request.form.get('amount', 0))
            from_currency = request.form.get('from_currency')
            to_currency = request.form.get('to_currency')

            if from_currency == to_currency:
                result = f"{amount} {from_currency} = {amount} {to_currency}"
            else:
                rate = exchange_rates.get(from_currency, {}).get(to_currency)
                if rate:
                    converted = amount * rate
                    result = f"{amount} {from_currency} = {round(converted, 2)} {to_currency}"
                else:
                    result = "Conversion rate not found."
        except ValueError:
            result = "Invalid amount entered."

    return render_template('converter.html', result=result, currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
