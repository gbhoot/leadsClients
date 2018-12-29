from flask import Flask, render_template, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "sssssssssssshhh"

@app.route('/')
def index():
    mysql = connectToMySQL('lead_gen_business')
    query = ("SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS full_name, "+
        "COUNT(leads.leads_ID) AS no_of_leads FROM clients "+
        "LEFT JOIN sites ON clients.client_id = sites.client_id "+
        "LEFT JOIN leads ON sites.site_id = leads.site_id "+
        "GROUP BY clients.client_id;")
        # "WHERE" need to add date algoritm)
    
    customers = mysql.query_db(query)
    customerNames = []
    customerLeads = []
    for customer in customers:
        customerNames.append(str(customer['full_name']))
        customerLeads.append(int(customer['no_of_leads']))
    # print(customers)
    print(customerLeads)

    return render_template("index.html", customers = customers, names = customerNames, 
        leads = customerLeads)

if __name__ == "__main__":
    app.run(debug=True)