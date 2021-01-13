<template>
    <v-container>
        <h1>Enemy Finder</h1>
        <br>
        <v-row>
            <v-text-field v-model="search" label="Search" solo append-icon="mdi-magnify"></v-text-field>
        </v-row>
        <v-row>
            <v-spacer></v-spacer>
            <v-flex class="xs d-flex align-center">
                <h3>Filter: </h3>
            </v-flex>
            <v-flex xs2>
                <v-select :items="selectItems" label="Attributes" v-model="attr" @change="find()"/>
            </v-flex>
            <v-spacer></v-spacer>
            <v-flex xs5 d-flex justify-center align-center>
                <v-text-field  mx-4 type="number" v-model="lwrBound" label="Lower Bound" @change="find()" append-icon="mdi-close" @click:append="lwrBound = null; find()"></v-text-field>
                <h3 style="margin: 10px;"> &nbsp;-&nbsp;</h3>
                <v-text-field  mx-4 type="number" v-model="upperBound" label="Upper Bound" @change="find()" append-icon="mdi-close" @click:append="lwrBound = null; find()"></v-text-field>
            </v-flex>
            <v-spacer></v-spacer>
            <v-flex xs2 d-flex align-center>
                <v-btn color="secondary" @click="find()"> Apply</v-btn>
            </v-flex>
        </v-row>
        <!-- <v-row>
            <v-btn @click="find()" block color="secondary"> Find</v-btn>
        </v-row> -->
        <br>
        <v-row>
            <v-spacer></v-spacer>
            <v-flex xs12>
               <v-data-table :headers="headers" :items="resultTable" :search="search">
                    <template v-slot:item.image="{ item }">
                        <div class="p-2">
                            <v-img :src="require(`@/assets/img/enemy/${item.key}.png`)" :alt="item.name" height="75" width="75"></v-img>
                        </div>
                    </template>
                    <template v-slot:item.stages="{item}">
                        <div style="padding: 5px;">
                            <v-chip v-for="i in item.stages" :key="`${item.key}-stages-${i}`" style="margin: 1px;">{{getCode(i)}}</v-chip>
                        </div>
                    </template>
               </v-data-table>
            </v-flex>
            <v-spacer></v-spacer>
        </v-row>
    </v-container>
</template>

<script>
import enemies from "@/assets/data/en-US/gamedata/levels/enemydata/enemy_database.json"
import enemy_stages from "@/assets/processed/enemy_stages.json"
import stage_table from "@/assets/data/en-US/gamedata/excel/stage_table.json"
export default {
    data: () => ({
        enemies: enemies.enemies,
        enemy_stages: enemy_stages,
        stage_table: stage_table,
        attr: "atk",
        lwrBound: null,
        upperBound: null,
        selectItems: [
            {text: "ATK", value: "atk"},
            {text: "DEF", value: "def"},
            {text: "Max HP", value: "maxHp"},
            {text: "RES", value: "magicResistance"}
        ],
        result: [],
        search: "",
        headers: [
            {text: "Image", value: 'image'},
            {text: "Name", value: 'name', width: 250},
            {text: "Max HP", value: 'maxHp'},
            {text: "ATK", value: 'atk'},
            {text: "DEF", value: 'def'},
            {text: "RES", value: 'magicResistance'},
            {text: "Stages", value: 'stages',width: 500}

        ],
        resultTable: [],
    }),
    methods: {
        find: function(){
            this.result = []
            this.resultTable = []
            this.enemies.forEach(it => {
                let val = it.Value[0].enemyData.attributes[this.attr].m_value
                if((!this.lwrBound || val >= this.lwrBound) && (!this.upperBound || val <= this.upperBound)) {
                    this.result.push(it)
                    let entry = {
                        key: it.Key,
                        image: `@/src/assets/img/enemy/${it.Key}.png`,
                        name: it.Value[0].enemyData.name.m_value,
                        atk: it.Value[0].enemyData.attributes.atk.m_value, 
                        def: it.Value[0].enemyData.attributes.def.m_value,
                        maxHp: it.Value[0].enemyData.attributes.maxHp.m_value,
                        magicResistance: it.Value[0].enemyData.attributes.magicResistance.m_value,
                        stages: this.enemy_stages[it.Key]
                    }
                    this.resultTable.push(entry)
                }
            })
        },
        getCode: function(stageId){
            let sid = stageId.replace("level_","").replace("weekly", "wk").replace("promote", "pro").replace("killcost","kc")
            let s =  stage_table.stages[sid];
            if (s.code === "Annihilation") {
                return s.code + " " + stageId[stageId.length-1]
            }
            return s.code
        }
    },
    mounted: function() {
        this.find()
    }
}
</script>

<style>

</style>