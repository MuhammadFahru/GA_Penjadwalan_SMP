# Import Library atau Package
from flask import Flask, request, render_template
import json
from json2html import *

import os
clear = lambda: os.system('cls')

from functions import generate_population
from functions import selection
from functions import crossover
from functions import mutation
from functions import reassign_gen
from functions import filter_guru

from copy import deepcopy

# Init Flask
app = Flask(__name__)

# Route beranda atau halaman awal
@app.route("/")
# Function index
def index():
    # Render template
    return render_template('index.html')

# Route generate
@app.route("/generate")
# Function generate
def generate():
    # Jumlah kebutuan mapel
    mapel = 10
    # Render template
    return render_template('generate.html', mapel = mapel)

# Route process
@app.route("/process", methods=['POST'])
# Function process
def process():
    # Get Data From Request
    dataForm = request.form.to_dict(flat=False)
    
    # Create dataInput as Dict Data
    dataInput = {
      "Kelas": {
          "VII": [
              "A",
              "B",
              "C",
              "D",
              "E",
              "F",
              "G",
              "H",
              "I",
              "J"
          ],
          "VIII": [
              "A",
              "B",
              "C",
              "D",
              "E",
              "F",
              "G",
              "H",
              "I",
              "J"
          ],
          "IX": [
              "A",
              "B",
              "C",
              "D",
              "E",
              "F",
              "G",
              "H",
              "I",
              "J"
          ]
      },
      "Waktu": {
          "Senin": [
              "7:00 - 7:40",
              "7:40 - 8:20",
              "8:20 - 9:00",
              "9:40 - 10:20",
              "10:20 - 11:00",
              "11:00 - 11:40",
              "12:20 - 13:00",
              "13:00 - 13:40"
          ],
          "Selasa": [
              "7:00 - 7:40",
              "7:40 - 8:20",
              "8:20 - 9:00",
              "9:40 - 10:20",
              "10:20 - 11:00",
              "11:00 - 11:40",
              "12:20 - 13:00",
              "13:00 - 13:40"
          ],
          "Rabu": [
              "7:00 - 7:40",
              "7:40 - 8:20",
              "8:20 - 9:00",
              "9:40 - 10:20",
              "10:20 - 11:00",
              "11:00 - 11:40",
              "12:20 - 13:00",
              "13:00 - 13:40"
          ],
          "Kamis": [
              "7:00 - 7:40",
              "7:40 - 8:20",
              "8:20 - 9:00",
              "9:40 - 10:20",
              "10:20 - 11:00",
              "11:00 - 11:40",
              "12:20 - 13:00",
              "13:00 - 13:40"
          ],
          "Jumat": [
              "7:00 - 7:40",
              "7:40 - 8:20",
              "8:20 - 9:00",
              "9:40 - 10:20",
              "10:20 - 11:00",
              "11:00 - 11:40"
          ]
      },
      "List_Mapel": []
    }
    
    # For Iteration ID
    id_iter = 0
    
    # Looping
    for index, mapel in enumerate(dataForm["Mapel"]):
      # Jika Alokasi Jam sama dengan 4 jam
      if int(dataForm["Alokasi_Jam"][index]) == 4:
        id_iter = id_iter + 1
        dict_data = {
            "ID": str(id_iter),
            "Mapel": mapel,
            "Alokasi_Jam": "2",
            "Guru": {
              "VII": [
                dataForm["GuruTujuh1"][index],
                dataForm["GuruTujuh2"][index]
              ],
              "VIII": [
                dataForm["GuruDelapan1"][index],
                dataForm["GuruDelapan2"][index]
              ],
              "IX": [
                dataForm["GuruSembilan1"][index],
                dataForm["GuruSembilan2"][index]
              ]
            }
        }
        dataInput["List_Mapel"].append(dict_data)
        id_iter = id_iter + 1
        dict_data = {
            "ID": str(id_iter),
            "Mapel": mapel,
            "Alokasi_Jam": str(int(dataForm["Alokasi_Jam"][index]) - 2),
            "Guru": {
              "VII": [
                dataForm["GuruTujuh1"][index],
                dataForm["GuruTujuh2"][index]
              ],
              "VIII": [
                dataForm["GuruDelapan1"][index],
                dataForm["GuruDelapan2"][index]
              ],
              "IX": [
                dataForm["GuruSembilan1"][index],
                dataForm["GuruSembilan2"][index]
              ]
            }
        }
        dataInput["List_Mapel"].append(dict_data)
      elif int(dataForm["Alokasi_Jam"][index]) > 4:
        id_iter = id_iter + 1
        dict_data = {
            "ID": str(id_iter),
            "Mapel": mapel,
            "Alokasi_Jam": "3",
            "Guru": {
              "VII": [
                dataForm["GuruTujuh1"][index],
                dataForm["GuruTujuh2"][index]
              ],
              "VIII": [
                dataForm["GuruDelapan1"][index],
                dataForm["GuruDelapan2"][index]
              ],
              "IX": [
                dataForm["GuruSembilan1"][index],
                dataForm["GuruSembilan2"][index]
              ]
            }
        }
        dataInput["List_Mapel"].append(dict_data)
        id_iter = id_iter + 1
        dict_data = {
            "ID": str(id_iter),
            "Mapel": mapel,
            "Alokasi_Jam": str(int(dataForm["Alokasi_Jam"][index]) - 3),
            "Guru": {
              "VII": [
                dataForm["GuruTujuh1"][index],
                dataForm["GuruTujuh2"][index]
              ],
              "VIII": [
                dataForm["GuruDelapan1"][index],
                dataForm["GuruDelapan2"][index]
              ],
              "IX": [
                dataForm["GuruSembilan1"][index],
                dataForm["GuruSembilan2"][index]
              ]
            }
        }
        dataInput["List_Mapel"].append(dict_data)
      elif int(dataForm["Alokasi_Jam"][index]) < 4:
        id_iter = id_iter + 1
        dict_data = {
            "ID": str(id_iter),
            "Mapel": mapel,
            "Alokasi_Jam": dataForm["Alokasi_Jam"][index],
            "Guru": {
              "VII": [
                dataForm["GuruTujuh1"][index],
                dataForm["GuruTujuh2"][index]
              ],
              "VIII": [
                dataForm["GuruDelapan1"][index],
                dataForm["GuruDelapan2"][index]
              ],
              "IX": [
                dataForm["GuruSembilan1"][index],
                dataForm["GuruSembilan2"][index]
              ]
            }
        }
        dataInput["List_Mapel"].append(dict_data)

    # Write
    with open('input.json', 'w') as input:
      json.dump(dataInput, input, indent=4)
    
    # Baca data json
    def load_data(path):
        with open(path, 'r') as read_file:
            data = json.load(read_file)

        return data

    # Masukan data json ke variabel
    data = load_data('input.json')
    # Menyaring data Guru pada Mapel menjadi unique
    filter_guru.filter_guru(data)

    # Parameter
    gen_num = 4 # Banyaknya individu dalam populasi
    laju_mutasi = 0.04
    population = generate_population.generate_population(gen_num, data)
    max_generation = 100 # batas maksimal iterasi

    # Main Looping
    i = 0
    for i in range(0, max_generation):
        # Logging
        if i % 10 == 0:
            clear()
            print("Iteration: " + str(i))
            j = 1
            for individu in population:
                print("\nIndividu-"+ str(j))
                # Cost-1 = Mapel yang dibagi 2 tetapi terdapat pada satu hari 
                print("Cost-1: " + str(individu['Cost_cons1']))
                # Cost-2 = Konflik jadwal guru yang mengajar kelas berbeda tetapi pada saat waktu yang sama
                print("Cost-2: " + str(individu['Cost_cons2']))
                print("Total Cost: "+ str(individu['Cost']))
                j += 1

        # Terminate ketika semua constrains satisfied
        if population[0]['Cost'] == 0:
            break

        # Seleksi
        parent1, parent2 = deepcopy(selection.selection(population))
        # Crossover
        child1, child2 = deepcopy(crossover.crossover(parent1, parent2, data))
        # Mutasi
        mutation.mutation_func(child1, data, laju_mutasi)
        mutation.mutation_func(child2, data, laju_mutasi)
        # Masukkan individu hasil mutasi ke populasi
        reassign_gen.reassign(population, child1, child2)  

    # Fungsi untuk menulis hasil solusi/gen/kromosom/individu ke file
    def write_data(data, path):
        with open(path, 'w') as write_file:
            json.dump(data, write_file, indent=4)

    # Ambil timetable terbaik lalu tuliskan ke file
    write_data(population[0]['Timetable'], 'output.json')

    # Read
    with open('output.json', 'r') as output:
      fileData = json.load(output)
    
    # Kelas 7
    table_data_7_a = json2html.convert(json=fileData["VII"]["A"], table_attributes="id=\"data-table\"")
    table_data_7_b = json2html.convert(json=fileData["VII"]["B"], table_attributes="id=\"data-table\"")
    table_data_7_c = json2html.convert(json=fileData["VII"]["C"], table_attributes="id=\"data-table\"")
    table_data_7_d = json2html.convert(json=fileData["VII"]["D"], table_attributes="id=\"data-table\"")
    table_data_7_e = json2html.convert(json=fileData["VII"]["E"], table_attributes="id=\"data-table\"")
    table_data_7_f = json2html.convert(json=fileData["VII"]["F"], table_attributes="id=\"data-table\"")
    table_data_7_g = json2html.convert(json=fileData["VII"]["G"], table_attributes="id=\"data-table\"")
    table_data_7_h = json2html.convert(json=fileData["VII"]["H"], table_attributes="id=\"data-table\"")
    table_data_7_i = json2html.convert(json=fileData["VII"]["I"], table_attributes="id=\"data-table\"")
    table_data_7_j = json2html.convert(json=fileData["VII"]["J"], table_attributes="id=\"data-table\"")
    
    # Kelas 8
    table_data_8_a = json2html.convert(json=fileData["VIII"]["A"], table_attributes="id=\"data-table\"")
    table_data_8_b = json2html.convert(json=fileData["VIII"]["B"], table_attributes="id=\"data-table\"")
    table_data_8_c = json2html.convert(json=fileData["VIII"]["C"], table_attributes="id=\"data-table\"")
    table_data_8_d = json2html.convert(json=fileData["VIII"]["D"], table_attributes="id=\"data-table\"")
    table_data_8_e = json2html.convert(json=fileData["VIII"]["E"], table_attributes="id=\"data-table\"")
    table_data_8_f = json2html.convert(json=fileData["VIII"]["F"], table_attributes="id=\"data-table\"")
    table_data_8_g = json2html.convert(json=fileData["VIII"]["G"], table_attributes="id=\"data-table\"")
    table_data_8_h = json2html.convert(json=fileData["VIII"]["H"], table_attributes="id=\"data-table\"")
    table_data_8_i = json2html.convert(json=fileData["VIII"]["I"], table_attributes="id=\"data-table\"")
    table_data_8_j = json2html.convert(json=fileData["VIII"]["J"], table_attributes="id=\"data-table\"")
    
    # Kelas 9
    table_data_9_a = json2html.convert(json=fileData["IX"]["A"], table_attributes="id=\"data-table\"")
    table_data_9_b = json2html.convert(json=fileData["IX"]["B"], table_attributes="id=\"data-table\"")
    table_data_9_c = json2html.convert(json=fileData["IX"]["C"], table_attributes="id=\"data-table\"")
    table_data_9_d = json2html.convert(json=fileData["IX"]["D"], table_attributes="id=\"data-table\"")
    table_data_9_e = json2html.convert(json=fileData["IX"]["E"], table_attributes="id=\"data-table\"")
    table_data_9_f = json2html.convert(json=fileData["IX"]["F"], table_attributes="id=\"data-table\"")
    table_data_9_g = json2html.convert(json=fileData["IX"]["G"], table_attributes="id=\"data-table\"")
    table_data_9_h = json2html.convert(json=fileData["IX"]["H"], table_attributes="id=\"data-table\"")
    table_data_9_i = json2html.convert(json=fileData["IX"]["I"], table_attributes="id=\"data-table\"")
    table_data_9_j = json2html.convert(json=fileData["IX"]["J"], table_attributes="id=\"data-table\"")
    
    return render_template('result.html',
      table_data_7_a = table_data_7_a,
      table_data_7_b = table_data_7_b,
      table_data_7_c = table_data_7_c,
      table_data_7_d = table_data_7_d,
      table_data_7_e = table_data_7_e,
      table_data_7_f = table_data_7_f,
      table_data_7_g = table_data_7_g,
      table_data_7_h = table_data_7_h,
      table_data_7_i = table_data_7_i,
      table_data_7_j = table_data_7_j,
      table_data_8_a = table_data_8_a,
      table_data_8_b = table_data_8_b,
      table_data_8_c = table_data_8_c,
      table_data_8_d = table_data_8_d,
      table_data_8_e = table_data_8_e,
      table_data_8_f = table_data_8_f,
      table_data_8_g = table_data_8_g,
      table_data_8_h = table_data_8_h,
      table_data_8_i = table_data_8_i,
      table_data_8_j = table_data_8_j,
      table_data_9_a = table_data_9_a,
      table_data_9_b = table_data_9_b,
      table_data_9_c = table_data_9_c,
      table_data_9_d = table_data_9_d,
      table_data_9_e = table_data_9_e,
      table_data_9_f = table_data_9_f,
      table_data_9_g = table_data_9_g,
      table_data_9_h = table_data_9_h,
      table_data_9_i = table_data_9_i,
      table_data_9_j = table_data_9_j
    )

# Route team
@app.route("/team")
# Function team
def team():
    # Render template
    return render_template('team.html')

# Driver
if __name__ == '__main__':
    app.run(debug=True)