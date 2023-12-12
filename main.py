from flask import Flask, request, send_file
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        # メモリ内にファイルを読み込む
        file_stream = io.BytesIO()
        file.save(file_stream)
        file_stream.seek(0)

        file_name = file.filename

        

        # メモリ内のファイルストリームを送信
        return send_file(
                        file_stream,
                        download_name=file_name,
                        as_attachment=True,
                        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                        )

    return '''
    <!doctype html>
    <title>ファイルアップロード</title>
    <h1>Excelファイルをアップロードしてください</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=アップロード>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
