def get_file_extension(fname):
    return fname.split('.')[0]

def save_report(df, fname):
    
    print("Report generated in", fname)

def generate_pivot(datafile):
    df = pd.read_csv(datafile)
    return df

def get_report_filename(fname):
    filename = fname[:-4]
    res = f'{filename}_report.xlsx'
    return res

def usage(prog_name):
    print(f'python {prog_name} excel_file')

def main(args):
    excel_file = sys.argv[1]
    rprt_file = get_report_filename(excel_file)
    pvt_data = generate_pivot(excel_file)
    save_report(pvt_data, rprt_file)

# Main starts from here
if __name__ == "__main__":
    import sys
    main(sys.argv)
