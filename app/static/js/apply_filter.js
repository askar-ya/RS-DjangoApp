function apply_filters() {
    let main_box = this.parentElement.parentElement

    let q_where = main_box.querySelector('#q_where')

    console.log(q_where.value);

    let param = []

    let ignore = main_box.querySelector('#ignore').value
    let ignore_array = ''
    ignore = ignore.replaceAll('@', '').replaceAll(' ', '').split(',')
    for (let i = 0; i < ignore.length; i++) {
        if (ignore[i] !== '') {
            let prefix = '&ignore=' + ignore[i]
            ignore_array += prefix
        }
    }
    if (ignore_array !== '') {
        param.push(ignore_array)
    }


    let counts_filters = [
        'q', 'q_where',
        'subs_start', 'subs_end',
        'views_start', 'views_end',
        'like_start', 'like_end',
        'comment_start', 'comment_end'
    ]

    for (let i = 0; i < counts_filters.length; i++) {
        let value = main_box.querySelector('#' + counts_filters[i]).value
        console.log(value)
        if (value !== '') {
            param.push(counts_filters[i] + '=' + value)
        }
    }

    param = param.join('&')

    let url = 'http://reelsscanner.com/app/search/?'
    console.log(url + param)
    window.location.replace(url + param)
}