const { encoder, Field } = require('tetris-fumen');

const pages = [];
pages.push({
    field: Field.create(
        'LLL_______' +
        'LOO_______' +
        'JOO_______' +
        'JJJ_______',
        'XXXXXXXXX_',
    ),
    comment: 'Perfect Clear Opener',
});

pages.push({
    operation: {
        type: 'T', rotation: 'left', x: 9, y: 1,
    },
});

pages.push({
    operation: {
        type: 'Z', rotation: 'spawn', x: 7, y: 0,
    },
});

pages.push({
    operation: {
        type: 'S', rotation: 'spawn', x: 8, y: 2,
    },
});

pages.push({
    comment: 'Success: 61.19 %',
    flags: {
        mirror: true,
    },
});

pages.push({
    comment: '(Mirror)',
});

console.log(encoder.encode(pages));  // v115@9gilGeglRpGeg...../~/.....ciNEyoAVB