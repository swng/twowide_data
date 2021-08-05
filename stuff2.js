// process getRush.json and generate out.csv of puzzle details

const createCsvWriter = require('csv-writer').createObjectCsvWriter;

const fs = require('fs');

const { encoder, Field } = require('tetris-fumen');

function toFumenString(board) {
	result = '';
	for (let row = 0; row < board.length; row++) {
		for (let col = 0; col < board[row].length; col++) {
			a = board[row][col];
			if (a == 0 || a == '0') {
				result += '_';
			}
			if (a == 1 || a == '1') {
				result += 'Z';
			}
			if (a == 2 || a == '2') {
				result += 'L';
			}
			if (a == 3 || a == '3') {
				result += 'O';
			}
			if (a == 4 || a == '4') {
				result += 'S';
			}
			if (a == 5 || a == '5') {
				result += 'I';
			}
			if (a == 6 || a == '6') {
				result += 'J';
			}
			if (a == 7 || a == '7') {
				result += 'T';
			}
			if (a == 8 || a == '8') {
				result += 'X';
			}
		}
	}
	return result;
}

let rawdata = fs.readFileSync('getRush.json');
let data = JSON.parse(rawdata);

processed = []
last = 0;
for (i = 0; i < data.length; i++) {
    last++;
    while (last != data[i]['id']) {
        temp = {
            id: last,
            pieces: "",
            hold: "",
            goal: "",
            fumen: "",
            solution: "",
        }
        processed.push(temp);
        last++;
    }

    board = data[i]['board'];
    
    const pages = [];
	pages.push({
		field: Field.create(toFumenString(board)),
	});
    fumen = encoder.encode(pages);

    temp = {
        id: data[i]['id'],
        pieces: data[i]['pieces'],
        hold: data[i]['held'],
        goal: data[i]['goals']['lines_sent'],
        fumen: 'https://harddrop.com/fumen/?' + fumen,
        solution: "?"
    }
    processed.push(temp);

	//console.log(i, data[i]['id']);

}



const csvWriter = createCsvWriter({
	path: 'out.csv',
	header: [
		{ id: 'id', title: 'ID' },
		{ id: 'pieces', title: 'Pieces' },
		{ id: 'hold', title: 'Hold' },
		{ id: 'goal', title: 'Goal' },
        { id: 'fumen', title: 'Fumen' },
        { id: 'solution', title: 'Solution' },
	],
});

csvWriter
  .writeRecords(processed)
  .then(()=> console.log('The CSV file was written successfully'));