# Automated-Exam-Evaluation
An Optical Character Recognition and Natural Language Processing based automated exam evaluation system

### Functionalities:
- OCR
- Check a question (one line answer)
- Check a question (descriptive answer - In Progress)

### Usage

1. Clone/Download the repository

2. In the downloaded directory, run the command below in command prompt/terminal to install all the dependencies.
```sh
$ npm install
```

3. Run the app using
```sh
$ node server
```

4. Visit http://localhost:3000, you should see it  running!

### Flow
1. Upload an image.
2. It will open image preview, Outputs: OCR and final score using cosine similarity.
3. User can also manage previous uploads.
