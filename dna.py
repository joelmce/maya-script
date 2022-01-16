class DNA:
    DNA_DELIMITER = "-"

    def __init__(self, supply):
        self.supply = supply

    def create_dna(_layers):
        randNum = []
        for layer in _layers:
            totalWeight = 0

            for element in layer.elements:
                totalWeight += element.weight

            random = math.floor(random.randint(1, 999) * totalWeight)

            i = 0
            while i < len(layer.elements):
                random -= layer.elements[i].weight
                if(random < 0):
                    return randNum.push(layer.elements[i])
        return randNum.join(DNA_DELIMITER)

    def filter_dna_options(_dna):
        dnaItems = _dns.split(DNA_DELIMITER)
        filteredDNA = filter(queryDNA, element) # Needs revision
        return filteredDNA.join(DNA_DELIMITER)

    def remove_query(_dna):
        query = /(\?.*$/)
        return _dna.replace(query, "")

    def query_dna():
        query = /(\?.*$/)
        queryString = query.exec(element)
        if not queryString:
            return True

    def is_dna_unique(_dnaList = set(), _dna = ""):
        _filteredDNA = filterDNAOptions(_dna)
        if _filteredDNA not in _dnaList:
            return True
