// oh my god I got async working I can actually do multiple at once thank god
// process getRush.json and post puzzle details to discord
// image generation code stolen from fumen-canvas

const Discord = require('discord.js');
const { prefix, token } = require('./config.json');

const { createCanvas } = require('canvas');
const { decoder } = require('tetris-fumen');
const fs = require('fs');

const { encoder, Field } = require('tetris-fumen');

const colors = {
	I: { normal: '#41afde', highlight1: '#3dc0fb', highlight2: '#3dc0fb', lighter: '#3dc0fb', light: '#43d3ff' },
	T: { normal: '#b451ac', highlight1: '#d161c9', highlight2: '#d161c9', lighter: '#d161c9', light: '#e56add' },
	S: { normal: '#66c65c', highlight1: '#75d96a', highlight2: '#7cd97a', lighter: '#7cd97a', light: '#88ee86' },
	Z: { normal: '#ef624d', highlight1: '#ff7866', highlight2: '#ff8778', lighter: '#fd7660', light: '#ff9484' },
	L: { normal: '#ef9535', highlight1: '#ffa94d', highlight2: '#ffae58', lighter: '#fea440', light: '#ffbf60' },
	J: { normal: '#1983bf', highlight1: '#1997e3', highlight2: '#1997e3', lighter: '#1997e3', light: '#1ba6f9' },
	O: { normal: '#f7d33e', highlight1: '#ffe34b', highlight2: '#ffe34b', lighter: '#ffe34b', light: '#fff952' },
	X: { normal: '#686868', highlight1: '#686868', highlight2: '#686868', lighter: '#686868', light: '#949494' },
	Empty: { normal: '#f3f3ed' },
};

function draw(fumenPage, tilesize, numrows, transparent) {
	const field = fumenPage.field;
	const operation = fumenPage.operation;

	function operationFilter(e) {
		return i == e.x && j == e.y;
	}

	if (numrows == undefined) {
		numrows = 0;
		for (i = 0; i < 10; i++) {
			for (j = 0; j < 23; j++) {
				if (field.at(i, j) != '_') {
					numrows = Math.max(numrows, j);
				}
				if (operation != undefined && operation.positions().filter(operationFilter).length > 0) {
					numrows = Math.max(numrows, j);
				}
			}
		}
		numrows += 2;
	}
	const width = tilesize * 10;
	const height = numrows * tilesize;

	const canvas = createCanvas(width, height);
	const context = canvas.getContext('2d');

	if (!transparent) {
		context.fillStyle = colors['Empty'].normal;
	} else {
		context.fillStyle = 'rgba(0, 0, 0, 0)';
	}
	context.fillRect(0, 0, width, height);

	for (i = 0; i < 10; i++) {
		for (j = 0; j < numrows; j++) {
			if (field.at(i, j) != '_') {
				context.fillStyle = colors[field.at(i, j)].light;
				context.fillRect(
					i * tilesize,
					height - (j + 1) * tilesize - tilesize / 5,
					tilesize,
					tilesize + tilesize / 5
				);
			}
			if (operation != undefined && operation.positions().filter(operationFilter).length > 0) {
				context.fillStyle = colors[operation.type].light;
				context.fillRect(
					i * tilesize,
					height - (j + 1) * tilesize - tilesize / 5,
					tilesize,
					tilesize + tilesize / 5
				);
			}
		}
	}
	for (i = 0; i < 10; i++) {
		for (j = 0; j < numrows; j++) {
			if (field.at(i, j) != '_') {
				context.fillStyle = colors[field.at(i, j)].normal;
				context.fillRect(i * tilesize, height - (j + 1) * tilesize, tilesize, tilesize);
			}
			if (operation != undefined && operation.positions().filter(operationFilter).length > 0) {
				context.fillStyle = colors[operation.type].normal;
				context.fillRect(i * tilesize, height - (j + 1) * tilesize, tilesize, tilesize);
			}
		}
	}
	return canvas;
}

const GIFEncoder = require('gifencoder');

function drawFumens(fumenPages, tilesize, numrows, start, end, transparent) {
	if (end == undefined) {
		end = fumenPages.length;
	}
	if (numrows == undefined) {
		numrows = 0;
		function operationFilter(e) {
			return i == e.x && j == e.y;
		}
		for (x = start; x < end; x++) {
			field = fumenPages[x].field;
			operation = fumenPages[x].operation;
			for (i = 0; i < 10; i++) {
				for (j = 0; j < 23; j++) {
					if (field.at(i, j) != '_') {
						numrows = Math.max(numrows, j);
					}
					if (operation != undefined && operation.positions().filter(operationFilter).length > 0) {
						numrows = Math.max(numrows, j);
					}
				}
			}
		}
		numrows += 2;
	}
	numrows = Math.min(23, numrows);
	const width = tilesize * 10;
	const height = numrows * tilesize;
	const canvas = createCanvas(width, height);
	const ctx = canvas.getContext('2d');
	const encoder = new GIFEncoder(width, height);
	encoder.start();
	encoder.setRepeat(0); // 0 for repeat, -1 for no-repeat
	encoder.setDelay(500); // frame delay in ms
	encoder.setQuality(1); // image quality. 10 is default.
	if (transparent) {
		encoder.setTransparent('rgba(0, 0, 0, 0)');
	}
	for (x = start; x < end; x++) {
		encoder.addFrame(draw(fumenPages[x], tilesize, numrows, transparent).getContext('2d'));
	}
	return encoder;
}

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

async function messageI(i) {
    board = data[i]['board'];

    const pages = [];
    pages.push({
        field: Field.create(toFumenString(board)),
    });
    fumen = encoder.encode(pages);

    var outputfile = 'output.png';

    var canvas = draw(pages[0], 22, undefined, true);
    var buffer = canvas.toBuffer('image/png');
    fs.writeFileSync(outputfile, buffer);

    details = '';
    details += 'ID: ' + data[i]['id'] + '\n';
    details += 'Pieces: ' + data[i]['pieces'] + '\n';
    details += 'Hold: ' + data[i]['held'] + '\n';
    details += 'Goal: ' + data[i]['goals']['lines_sent'] + ' lines' + '\n';
    details += 'Fumen: ' + 'https://harddrop.com/fumen/?' + fumen;

	await client.channels.cache.get('873450299153596446').send(details);
    await client.channels.cache.get('873450299153596446').send({files: ['./output.png'] });

    console.log(i, data[i]['id']);
}

let rawdata = fs.readFileSync('getRush.json');
let data = JSON.parse(rawdata);



const client = new Discord.Client({ intents: [Discord.Intents.FLAGS.GUILDS, Discord.Intents.FLAGS.GUILD_MESSAGES] });

client.on('ready', async () => {
    for (let index = 0; index < 5; index++) {
        await messageI(index);
    }
});

client.login(token);

