from args import Args
from query import Query
from output import Output

if __name__ == '__main__':
    a = Args()
    a.get_args()

    q = Query(a.year_start, a.year_end)
    q.query_api()

    o = Output(q.year_start, q.year_end, q.all_gdp)
    o.output_gdp()
