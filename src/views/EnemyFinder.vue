<template>
    <v-container>
        <h1>Enemy Finder</h1>
        <br>
        <v-row>
            <v-flex xs3>
                <v-select :items="selectItems" label="Attributes" v-model="attr" @change="find()"/>
            </v-flex>
            <v-spacer></v-spacer>
            <v-flex xs3>
                <v-text-field type="number" v-model="lwrBound" label="Lower Bound" @change="find()"></v-text-field>
            </v-flex>
            <v-spacer></v-spacer>
            <v-flex xs3>
                <v-text-field type="number" v-model="upperBound" label="Upper Bound" @change="find()"></v-text-field>
            </v-flex>
            <v-spacer></v-spacer>
        </v-row>
        <!-- <v-row>
            <v-btn @click="find()" block color="secondary"> Find</v-btn>
        </v-row> -->
        <br>
        <br>
        <br>
        <v-row>
            <v-spacer></v-spacer>
            <v-flex xs12>
               <v-data-table :headers="headers" :items="resultTable" :search="search">
                    <template v-slot:top>
                        <v-text-field
                        v-model="search"
                        label="Search"
                        class="mx-4"
                        solo
                        append-icon="mdi-magnify"
                        ></v-text-field>
                    </template>
               </v-data-table>
            </v-flex>
            <v-spacer></v-spacer>
        </v-row>
    </v-container>
</template>

<script>
import enemies from "@/assets/data/en-US/gamedata/levels/enemydata/enemy_database.json"
export default {
    data: () => ({
        enemies: enemies.enemies,
        attr: "atk",
        lwrBound: 0,
        upperBound: 10000,
        selectItems: [
            {text: "ATK", value: "atk"},
            {text: "DEF", value: "def"}
        ],
        result: [],
        search: "",
        headers: [
            {text: "Key", value: 'key'},
            {text: "Name", value: 'name'},
            {text: "ATK", value: 'atk'},
            {text: "DEF", value: 'def'},
        ],
        resultTable: [],
    }),
    methods: {
        find: function(){
            this.result = []
            this.resultTable = []
            this.enemies.forEach(it => {
                let val = it.Value[0].enemyData.attributes[this.attr].m_value
                if(val >= this.lwrBound && val <= this.upperBound) {
                    this.result.push(it)
                    let entry = {
                        key: it.Key,
                        name: it.Value[0].enemyData.name.m_value,
                        atk: it.Value[0].enemyData.attributes.atk.m_value, 
                        def: it.Value[0].enemyData.attributes.def.m_value
                    }
                    this.resultTable.push(entry)
                }
            })
            
        }
    },
    mounted: function() {
        this.find()
    }
}
</script>

<style>

</style>