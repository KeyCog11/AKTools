<template>
    <v-container>
        <vue-markdown>
            {{content.default}}
        </vue-markdown>
    </v-container>
</template>

<script>
import VueMarkdown from 'vue-markdown'
export default {
    components: {
        VueMarkdown
    },
    data: () => ({
        content: null,
    }), 
    async mounted() {
        let md = this.$route.params.md
        try {
           this.content = require("raw-loader!@/markdowns/"+md)
        } catch {
            this.content = "404 Not Found"
        }
    }
}
</script>

<style>

</style>