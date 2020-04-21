export default {
    state: {
        tag: {
            list: [],
            item: null,
            default: {
                title: '',
                color: '#FF0000',
            },
        },
        todo: {
            list: [],
            item: null,
            default: {
                title: '',
                description: '',
                tags: []
            },
            tagFilter: []
        }
    }
}